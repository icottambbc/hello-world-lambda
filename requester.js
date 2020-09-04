var config = require('../../config');
import * as request from 'request';


  const requestDefaults = {
    pfx,
    passphrase: config.passphrase,
    strictSSL: process.env.ENVIRONMENT === 'live',
    time: true,
    timeout: 20000,
  };
  const restClient = request.defaults(requestDefaults);

  /**
   * Get the xml based on constructor set up.
   * @return {xml} or {buffer}.
   */
  const getXMLData = () => {
    const options = {
      method,
      url: this.url,
      headers: { 'Accept': 'application/xml' },
    };

    if(requestBody) {
      options['body'] = requestBody;
      options['json'] = true;
    } 

    restClient(options, (err, response, body) => {
      if (err) {
        return err;
      }
      const statusCode = response ? response.statusCode : 500;
      const statusMessage = response ? response.statusMessage : '';
      if (statusCode >= 200 && statusCode < 400) {
        // fs.writeFile('result/data.xml', body, 'utf8', () => {
        //   console.log('DONE - raw xml');
        // });
        return body;
      } else {
        let error = {
          statusCode: statusCode,
          message: statusMessage,
        };
        return error;
      }
    });
  }


export default getXMLData;