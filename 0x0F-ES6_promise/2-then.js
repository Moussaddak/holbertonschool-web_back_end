export default function handleResponseFromAPI(promise) {
  const r = new Promise((resolve, reject) => {
    if (promise instanceof Promise) {
      resolve({
        status: 200,
        body: 'success',
      });
    }
    reject(new Error());
  });
  r.then((() => {
    console.log('Got a response from the API');
  }
  ));
}
