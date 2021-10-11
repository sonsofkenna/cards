<script context="module">
  export const prerender = true;
</script>

<script>
  import { page } from '$app/stores';

  import Navbar from '$lib/navbar/navbar.svelte';

  import Fa from 'svelte-fa/src/fa.svelte';
  import { faThumbsUp } from '@fortawesome/free-solid-svg-icons';
  import { faShare } from '@fortawesome/free-solid-svg-icons';

  import { cards } from '../../stores';

  let liked = [];

  let cards_value = $cards;

  function toggleLikeCard(card) {
    if (card.liked) {
      card.liked = false;
      card.stats.likes--;
    } else {
      card.liked = true;
      card.stats.likes++;
    }

    cards_value = [...$cards];
    
    liked = cards.filter(card => card.liked);
  }

  function getCardPath(card) {
    return `${$page.host}/${card.author.nickname}/${card.id}` // Dynamic path generator
  }

  function copyCardPath(card) {
    navigator.clipboard.writeText(
      getCardPath(card)
    )

    card.stats.shares++;
    cards = [...cards];
  }
</script>

<Navbar />

<div class="cards">
  {#each cards_value as card}
    <div class="card">
      <div class="top">
        <!-- Author -->
        <img class="pfp" src={card.author.pfp} alt={card.author.nickname}>
        <h1>{card.author.first + " " + card.author.last}</h1>
        <h5 style="color:#6d6d6d;">{'@' + card.author.nickname}</h5>
      </div>
      <div class="middle">
        <!-- Content -->
        {card.content}
      </div>
      <div class="bottom">
        <!-- Stats -->
        <div class="stats">
          <span 
            class="likes" on:click={() => {toggleLikeCard(card)}}
            class:liked={card.liked}
          >
            <Fa icon={faThumbsUp} />
            <span class="stat">
              {card.stats.likes}
            </span>
          </span>
          <span class="shares" on:click={() => copyCardPath(card)}>
            <Fa icon={faShare} />
            <span class="stat">
              {card.stats.shares}
            </span>
          </span>
        </div>
      </div>
    </div>
  {/each}
</div>

<style>
  .cards {
    --primary: #1c1c1c;
    --secondary: #333333;
    --spacing: 3px;

    font-family: Arial, Helvetica, sans-serif;
  }

  .card {
    background-color: var(--secondary);
    color: white;
    padding: 5px;
    border-radius: 20px;
    max-width: 550px;
    margin: auto;
    margin-bottom: 18px;

    box-shadow: 0px 0px 10px .1px var(--primary);
  }

  .card * {
    margin: 0;
  }
  .top {
    /* display: flex; */
    background-color: var(--primary);
    border-radius: 15px 15px 0px 0px;
    padding: 10px;
    height: 50px;
    margin-bottom: var(--spacing);
  }

  .pfp {
    float: left;
    width: 50px;
    height: 50px;
    border-radius: 50%;
    margin-right: 5px;
  }

  .middle {
    background-color: var(--primary);
    padding: 10px;
    margin-bottom: var(--spacing);
    font-size: 2em;
    font-weight: 600;
  }

  .middle::selection {
    background-color: var(--secondary);
  }

  .bottom {
    background-color: var(--primary);
    border-radius: 0px 0px 15px 15px;
    padding: 10px;
    padding-right: 30%;
    padding-left: 30%;
  }

  .stats {
    display: flex;
    width: 100%;
    justify-content: space-between;
    font-size: 22px;

    user-select: none;
  }

  .likes:hover {
    cursor: pointer;
  }

  .liked {
    color: rgb(255, 65, 65);
  }

  .shares:hover {
    cursor: pointer;
    color: rgb(0, 155, 255);
  }

  .stat {
    color: white;
  }
</style>