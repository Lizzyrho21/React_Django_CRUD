import React from "react"; 
import { Button, Form, FormGroup, Input, Label } from "reactstrap";
import axios from "axios";

import { API_URL } from "../constants";


class NewStudentForm extends React.Component {
    state = { 
        pk: 0,
        name: "",
        email: "",
        document: "",
        phone: "",
    };


    componentDidMount() {
        if (this.props.student) {
            const {pk, name, document, email, phone } = this.props.student;
            this.setState({ pk, name, document, email, phone });
        }
    }
}

