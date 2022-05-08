function deleteNote(noteId) {
    fetch("/delete-note", {
      method: "POST",
      body: JSON.stringify({ noteId: noteId }),
    }).then((_res) => {
      window.location.href = "/forum";
    });
  }

  function deleteID(user_id) {
    fetch("/signout", {
      method: "POST",
      body: JSON.stringify({ user_id: user_id }),
    }).then((_res) => {
      window.location.href = "/whos_in";
    });
  }