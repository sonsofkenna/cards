import { writable } from "svelte/store";

function generateCards(times = 0) {
  let result = [];

  for (let i = 0; i < times; i++) {
    result.push({
      author: {
        first: "Kian",
        last: "McKenna",
        nickname: "cowboycodr",
        followers: 0,
        pfp: "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSwOAz9F23MraOeH5RtdAj883MB-ywpMIPYSv36fcSVFazd1DQANyabtJ3eKBgRw1_t2PM&usqp=CAU"
      },
      stats: {
        likes: 4,
        shares: 2
      },
      content: "Cards, the in-progress, open-source, simplistic retake of social media.",
      id: 41,
      liked: false,
    });
  }

  return result;
}

export const cards = writable(generateCards(9));