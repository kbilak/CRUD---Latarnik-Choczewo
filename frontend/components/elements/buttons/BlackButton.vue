<template>
	<button @click="handleClick" :class="computedClasses">
		{{ buttonText }}
		<span v-if="icon" class="mdi" :class="mdiClass"></span>
	</button>
</template>

<script>
export default {
	props: {
		icon: {
			type: Boolean,
			default: false
		},
		mdi: {
			type: String,
			default: ''
		},
		click: {
			type: Function,
			default: () => {}
		},
		buttonText: {
			type: String,
			default: 'Dodaj zawodnika'
		}
	},
	computed: {
		computedClasses() {
			return [
				'btn',
				'h-[40px]',
				'text-white',
				'bg-black',
				'hover:bg-[#101010]',
				'transition',
				'ease-in-out',
				'duration-300',
				'rounded-[0.5rem]',
				'text-[1rem]',
				'font-medium',
				'px-4',
				'py-1',
				'w-auto',
				'flex',
				'items-center',
				'justify-center',
				'font-inter',
				'leading-[1.5]',
				'tracking-[0.005em]',
			]
		},
		mdiClass() {
			return `mdi-${this.mdi}`;
		}
	},
	methods: {
		handleClick() {
			this.click();
		}
	}
};
</script>