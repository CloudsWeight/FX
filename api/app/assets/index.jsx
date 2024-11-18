import React, {useEffect, useState } from 'react';
import ReactDOM from 'react-dom';
const Jsonlist = () => {
	const [data, setData] = useState([]);
	const [loading, setLoading] = useState(true);
	const [error, setError] = useState(null);

	useEffect(() => {

	fetch('http://localhost:43451/api/getNews')
	.then((response) => {
	if (!response.ok) {
		throw new Error(`${response.status} error`);
	}
	return response.json();
	})
	.then((json) => {
		setData(json);
		setLoading(false);
	})
	.catch((err) => {
		setError(err.message);
		setLoading(false);
	});
	}, []);

	if (loading) return <p> Loading...</p>;
	if (error) return <p> Error: {error}</p>;
	return (
		<div>
		<h1> List </h1>
		<ul>
			{data.map((item, index) => (
				<li key={index}>
				<strong>{item.key}:</strong> {item.value}
				</li>
				))}
		</ul>
		</div>
		);
	};

export default JsonList;
