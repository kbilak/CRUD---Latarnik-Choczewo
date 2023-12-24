<template>
	<button @click="handleClick" :class="computedClasses">
		{{ buttonText }}
		<input type="file" ref="fileInput" style="display: none;" @change="handleFileChange">
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
				'bg-blue-700',
				'hover:bg-blue-800',
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