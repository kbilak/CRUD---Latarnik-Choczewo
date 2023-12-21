<template>
	<button v-if="disabled" @click="handleClick" :class="computedClasses">
		<template v-if="!loading">
			{{ buttonText }}
			<span v-if="icon" class="mdi" :class="mdiClass"></span>
		</template>
		<template v-else>
			<div class="spinner"></div>
		</template>
	</button>
	<button v-else :class="computedClassesDisabled">
		<template v-if="!loading">
			{{ buttonText }}
			<span v-if="icon" class="mdi" :class="mdiClass"></span>
		</template>
		<template v-else>
			<div class="spinner"></div>
		</template>
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
		},
				loading: {
			type: Boolean,
			default: false
		},
		disabled: {
			type: Boolean,
			default: true
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
		computedClassesDisabled() {
			return [
				'btn',
				'h-[40px]',
				'text-white',
				'button-disabled',
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

<style>
@keyframes spin {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}

.spinner {
  border: 4px solid white;
  border-top: 4px solid black;
  border-radius: 50%;
  width: 20px;
  height: 20px;
  animation: spin 1s linear infinite;
}

.button-disabled {
    background-color: gray !important;
    cursor: auto !important;
}
.button-disabled:hover {
    background-color: gray !important;
}
</style>