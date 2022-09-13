function deepObjCopy(instance) {
  return JSON.parse(JSON.stringify(instance))
}

export {
  deepObjCopy
}
