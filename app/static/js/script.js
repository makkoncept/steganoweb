const legalFileTypes = ["image/png", "image/jpg", "image/jpeg"];

function handleImageUpload(event) {
  console.log(event.target.files[0]);
  const FileSize = event.target.files[0].size / 1024 / 1024; // in MB
  const fileType = event.target.files[0].type;
  if (FileSize > 2) {
    alert("File size exceeds 2 MB");
    event.target.value = ''
  } else if (!legalFileTypes.includes(fileType)) {
    alert("Only file of type 'jpeg', 'jpg', or 'png' allowed");
    event.target.value = ''
  } 
}
