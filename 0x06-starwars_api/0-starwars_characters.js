#!/usr/bin/node

const request = require('request-promise');

const movieId = process.argv[2];
const filmEndPoint = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

const getCharacters = async () => {
  try {
    const response = await request(filmEndPoint);
    const movieData = JSON.parse(response);
    return movieData.characters;
  } catch (error) {
    console.error('Error fetching movie data:', error.message);
    return [];
  }
};

const getCharacterNames = async () => {
  try {
    const characters = await getCharacters();
    const namePromises = characters.map(async (characterURL) => {
      try {
        const characterData = await request(characterURL);
        return JSON.parse(characterData).name;
      } catch (error) {
        console.error('Error fetching character data:', error.message);
        return '';
      }
    });
    const characterNames = await Promise.all(namePromises);
    console.log(characterNames.join('\n'));
  } catch (error) {
    console.error('Error fetching character names:', error.message);
  }
};

getCharacterNames();
