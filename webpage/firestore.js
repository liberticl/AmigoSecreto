const db = firebase.firestore();

export async function insertplayers(item) {
  try {
    const response = await db.collection("players").add(todo);
    return response;
  } catch (error) {
    throw new Error(error);
  }
}

export async function getSecretFriend(usermail) {
  try {
    let items = [];
    const response = await db
      .collection("players")
      .where("mail", "==", usermail)
      .get();

    response.forEach(function (item) {
        items.push(item.data());
    });

    const friend = items[0]["secretFriend"];
    const secret = getSecret(friend);
    
    return secret;
  } catch (error) {
    throw new Error(error);
  }
}

function getSecret(secret) {
    try {
        return atob(secret)
    } catch (err) {
        return atob(secret.slice(0,-1))
    }
}

export async function update(id, completed) {
  try {
    let docId;
    const doc = await db.collection("todos").where("id", "==", id).get();
    doc.forEach((i) => {
      docId = i.id;
    });

    await db.collection("todos").doc(docId).update({ completed: completed });
  } catch (error) {
    throw new Error(error);
  }
}
