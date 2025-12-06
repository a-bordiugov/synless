class NotesManager {
  constructor() {
    this.notes = [];
    this.selectedNotes = new Set();
    this.loadNotes();
    this.render();
  }

  loadNotes() {
    const notesData = JSON.parse(localStorage.getItem('notes'));
    if (notesData) {
      this.notes = Object.values(notesData);
    }
  }

  saveNotes() {
    const notesObj = {};
    this.notes.forEach((note) => {
      notesObj[`note_${note.id}`] = note;
    });
    localStorage.setItem('notes', JSON.stringify(notesObj));
  }

  add(content = '') {
    const newNote = {
      id: Date.now().toString(),
      content: content,
      createdAt: new Date().toISOString(),
      isEditing: false
    };

    this.notes.unshift(newNote);
    this.saveNotes();
    this.render();
    return newNote;
  }

  edit(noteId, newContent) {
    const noteIndex = this.notes.findIndex(note => note.id === noteId);
    if (noteIndex !== -1) {
      this.notes[noteIndex].isEditing = false;
      this.notes[noteIndex].content = newContent;
      this.notes[noteIndex].updatedAt = new Date().toISOString();
      this.saveNotes();
      this.render();
      return true;
    }
    return false;
  }

  remove(noteId) {
    const noteIndex = this.notes.findIndex(note => note.id === noteId);
    if (noteIndex !== -1) {
      const noteElement = document.querySelector(`[data-note-id="${noteId}"]`);
      if (noteElement) {
        noteElement.classList.add('note-removing');
        setTimeout(() => {
          this.notes.splice(noteIndex, 1);
          this.selectedNotes.delete(noteId);
          this.saveNotes();
          this.render();
        }, 200);
      }
      return true;
    }
    return false;
  }

  removeSelected() {
    if (this.selectedNotes.size === 0) return;

    if (!confirm(`Удалить ${this.selectedNotes.size} заметок?`)) {
      return;
    }

    this.selectedNotes.forEach(noteId => {
      const noteElement = document.querySelector(`[data-note-id="${noteId}"]`);
      if (noteElement) {
        noteElement.classList.add('note-removing');
      }
    });

    setTimeout(() => {
      this.notes = this.notes.filter(note => !this.selectedNotes.has(note.id));
      this.selectedNotes.clear();
      this.saveNotes();
      this.render();
    }, 200);
  }

  toggleSelect(noteId) {
    if (this.selectedNotes.has(noteId)) {
      this.selectedNotes.delete(noteId);
    } else {
      this.selectedNotes.add(noteId);
    }
    this.renderSelection();
  }

  renderSelection() {
    document.querySelectorAll('.note').forEach(noteElement => {
      const noteId = noteElement.dataset.noteId;
      const checkbox = noteElement.querySelector('.note-checkbox');
      if (checkbox) {
        checkbox.checked = this.selectedNotes.has(noteId);
      }

      if (this.selectedNotes.has(noteId)) {
        noteElement.classList.add('selected');
      } else {
        noteElement.classList.remove('selected');
      }
    });
  }

  render() {
    const notesContainer = document.querySelector('.notes');
    if (!notesContainer) return;

    notesContainer.innerHTML = '<div class="note new" id="new-note-btn"></div>';

    this.notes.forEach(note => {
      const noteElement = document.createElement('div');
      noteElement.className = 'note';
      noteElement.dataset.noteId = note.id;

      if (this.selectedNotes.has(note.id)) {
        noteElement.classList.add('selected');
      }

      const date = new Date(note.createdAt);
      const formattedDate = date.toLocaleDateString('ru-RU', {
        day: '2-digit',
        month: '2-digit',
        year: 'numeric',
        hour: '2-digit',
        minute: '2-digit'
      });

      if (note.isEditing) {
        noteElement.innerHTML = `
          <div class="note-header">
            <input type="checkbox" class="note-checkbox" 
                   onclick="notesManager.toggleSelect('${note.id}')"
                   ${this.selectedNotes.has(note.id) ? 'checked' : ''}>
            <div class="note-date">${formattedDate}</div>
          </div>
          <textarea id="edit-${note.id}" placeholder="Введите текст заметки...">${note.content}</textarea>
          <div class="note-actions">
            <button class="btn btn-save" onclick="notesManager.saveEdit('${note.id}')">
              Сохранить
            </button>
            <button class="btn btn-cancel" onclick="notesManager.cancelEdit('${note.id}')">
              Отмена
            </button>
          </div>
        `;
      } else {
        noteElement.innerHTML = `
          <div class="note-header">
            <input type="checkbox" class="note-checkbox" 
                   onclick="notesManager.toggleSelect('${note.id}')"
                   ${this.selectedNotes.has(note.id) ? 'checked' : ''}>
            <div class="note-date">${formattedDate}</div>
          </div>
          <div class="note-content">${note.content}</div>
          <div class="note-actions">
            <button class="btn btn-edit" onclick="notesManager.startEdit('${note.id}')">
              Редактировать
            </button>
            <button class="btn btn-delete" onclick="notesManager.remove('${note.id}')">
              Удалить
            </button>
          </div>
        `;
      }

      notesContainer.insertBefore(noteElement, notesContainer.firstChild);
    });

    const newNoteBtn = document.getElementById('new-note-btn');
    if (newNoteBtn) {
      newNoteBtn.addEventListener('click', () => {
        this.startNewNote();
      });
    }

    const bulkDeleteBtn = document.querySelector('.bulk-operations a');
    if (bulkDeleteBtn) {
      bulkDeleteBtn.onclick = (e) => {
        e.preventDefault();
        this.removeSelected();
      };

      bulkDeleteBtn.textContent = this.selectedNotes.size > 0
        ? `Удалить (${this.selectedNotes.size})`
        : 'Удалить';
    }
  }

  startEdit(noteId) {
    const noteIndex = this.notes.findIndex(note => note.id === noteId);
    if (noteIndex !== -1) {
      this.notes[noteIndex].isEditing = true;
      this.render();

      setTimeout(() => {
        const textarea = document.getElementById(`edit-${noteId}`);
        if (textarea) {
          textarea.focus();
        }
      }, 10);
    }
  }

  saveEdit(noteId) {
    const textarea = document.getElementById(`edit-${noteId}`);
    if (textarea) {
      const newContent = textarea.value.trim();
      this.edit(noteId, newContent);
    }
  }

  cancelEdit(noteId) {
    const noteIndex = this.notes.findIndex(note => note.id === noteId);
    if (noteIndex !== -1) {
      this.notes[noteIndex].isEditing = false;
      this.render();
    }
  }

  startNewNote() {
    this.notes.map(note => {
      if (note.isEditing) {
        this.cancelEdit(note.id);
      }
    });

    const newNote = this.add('');
    this.startEdit(newNote.id);
  }
}

let notesManager;