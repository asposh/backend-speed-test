package test

import (
	"crypto/tls"
	"encoding/json"
	"fmt"
	"io/ioutil"
	"net/http"
	"net/url"
)

// Client structure
type Client struct {
	Method string
	URL    string
	Data   map[string]interface{}
}

// Request - Make client request
func (ta *Client) Request() (int, map[string]interface{}) {
	resp, err := ta.getResponse()
	if err != nil {
		panic(err)
	}
	defer resp.Body.Close()

	body, err := ioutil.ReadAll(resp.Body)
	var jsonData map[string]interface{}
	if err := json.Unmarshal(body, &jsonData); err != nil {
		panic(err)
	}

	return resp.StatusCode, jsonData
}

// getClient - Get http client
func (ta *Client) getClient() *http.Client {
	transCfg := &http.Transport{
		TLSClientConfig: &tls.Config{InsecureSkipVerify: true},
	}
	client := &http.Client{Transport: transCfg}

	return client
}

// getResponse - Get response by method
func (ta *Client) getResponse() (*http.Response, interface{}) {
	client := ta.getClient()

	// POST method
	if ta.Method == "POST" {
		data := url.Values{}
		for key, value := range ta.Data {
			data.Add(key, fmt.Sprintf("%v", value))
		}
		return client.PostForm(ta.URL, data)
	}

	// GET method by default
	return client.Get(ta.URL)
}
