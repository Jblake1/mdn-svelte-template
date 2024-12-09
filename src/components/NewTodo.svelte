<!-- components/NewTodo.svelte -->
<script lang='ts'>
  import { createEventDispatcher, onMount } from 'svelte'
  const dispatch = createEventDispatcher()

  import { selectOnFocus } from '../actions'

  export let autofocus: boolean = false

  let name = ''
  let nameEl: HTMLElement     // reference to the name input DOM node


  let machine = ''
  let machineEl: HTMLElement

  let coffeeType = ''
  let coffeeTypeEl: HTMLElement

  let grinder = ''
  let grinderEl: HTMLElement

  let beanType = ''
  let beanTypeEl: HTMLElement

  const submit = async () => {
    try {
      const response = await fetch('http://localhost:4000/recommendation', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          machine,
          coffee_type: coffeeType,
          grinder,
          coffee_beans: beanType
        })
      });

      if (!response.ok) {
        throw new Error('Network response was not ok');
      }

      const data = await response.json();
      console.log(data);
    } catch (error) {
      console.error('There was a problem with the fetch operation:', error);
    }
  }

  const onCancel = () => {
    name = ''
    nameEl.focus()            // give focus to the name input
  }

  onMount(() => autofocus && nameEl.focus && nameEl.focus())    // if autofocus is true, we run nameEl.focus()

</script>

<form on:submit|preventDefault={submit} on:keydown={e => e.key === 'Escape' && onCancel()}>
  <h2 class="label-wrapper">
    <label for="machine" class="label__lg">Coffee Machine</label>
  </h2>
  <input bind:value={machine} bind:this={machineEl} use:selectOnFocus 
    type="text" id="machine" autoComplete="off" class="input input__lg" 
  />

  <h2 class="label-wrapper">
    <label for="coffeeType" class="label__lg">Coffee Type</label>
  </h2>
  <input bind:value={coffeeType} bind:this={coffeeTypeEl} use:selectOnFocus 
    type="text" id="coffeeType" autoComplete="off" class="input input__lg" 
  />

  <h2 class="label-wrapper">
    <label for="grinder" class="label__lg">Grinder Type</label>
  </h2>
  <input bind:value={grinder} bind:this={grinderEl} use:selectOnFocus 
    type="text" id="grinder" autoComplete="off" class="input input__lg" 
  />

  <h2 class="label-wrapper">
    <label for="beanType" class="label__lg">Bean Type</label>
  </h2>
  <input bind:value={beanType} bind:this={beanTypeEl} use:selectOnFocus 
    type="text" id="beanType" autoComplete="off" class="input input__lg" 
  />
  <button type="submit" disabled={false} class="btn btn__primary btn__lg">Submit</button>
</form>
