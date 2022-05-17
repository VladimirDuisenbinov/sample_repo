import React from 'react';
import axios from 'axios';
import styled from "styled-components";
import Container from 'react-bootstrap/Container';
import {Form as RBForm} from 'react-bootstrap';

const theme = {
    blue: {
      default: "#3f51b5",
      hover: "#283593"
    },
};

const Button = styled.button`
    background-color: ${(props) => theme[props.theme].default};
    color: white;
    padding: 5px 15px;
    border-radius: 5px;
    outline: 0;
    text-transform: uppercase;
    margin: 10px 0px;
    cursor: pointer;
    box-shadow: 0px 2px 2px lightgray;
    transition: ease background-color 250ms;
    &:hover {
    background-color: ${(props) => theme[props.theme].hover};
    }
    &:disabled {
    cursor: default;
    opacity: 0.7;
    }
`;

Button.defaultProps = {
    theme: "blue"
};

class Form extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            originalURL: '',
            shortURL: '',
            redirectURL: '',
        };

        this.handleChange = this.handleChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
    }
  
    handleChange(event) {
        this.setState({originalURL: event.target.value});
    }
  
    handleSubmit(event) {
        event.preventDefault();

        const env = process.env
        const BASE_URL = `${env.REACT_APP_BACKEND_URL}:${env.REACT_APP_BACKEND_PORT}`

        axios.post(
            `${BASE_URL}/url-shorts/`,
            {
                'url': this.state.originalURL
            }
        )
        .then(response => {
            const shortURL = response.data.data.short_url;

            this.setState(
                {
                    shortURL: shortURL,
                    redirectURL: `${BASE_URL}/redirect/${shortURL}/`
                }
            );
        })
        .catch(err => {
            const error = err.response.data.error
            console.log(error)
            const type = error.type
            const message = error.message

            alert(`${type}: ${message}`);
        })
    }
  
    render() {
        return (
            <Container>
                <RBForm>
                    <RBForm.Group controlId="originalURL">
                        <RBForm.Label>Original URL</RBForm.Label>
                        <RBForm.Control
                            type="text"
                            placeholder="e.g. https://google.nl"
                            value={this.state.originalURL}
                            onChange={this.handleChange}
                        />
                    </RBForm.Group>
                    <div>
                        <Button onClick={this.handleSubmit}>Submit</Button>
                    </div>
                    {
                        this.state.shortURL.length > 0
                        &&
                        <div>
                            <a href={this.state.redirectURL}>Press to redirect directly</a>
                            <p>
                                OR copy and paste this to your browser: <i>{this.state.redirectURL}</i>
                            </p>
                        </div>

                    }
                </RBForm>
            </Container>
        );
    }
}
  
export default Form;