export default function (length, position, value) {
  const viewData = new DataView(new ArrayBuffer(length));
  if (position > length) {
    throw new Error('Position outside range');
  }
  viewData.setInt8(position, value);
  return viewData;
}
