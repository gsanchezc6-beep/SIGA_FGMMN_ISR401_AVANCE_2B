function conectarSocket() {
  return io({ autoConnect: true });
}
