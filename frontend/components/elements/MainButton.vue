<template>
    <button :class="computedClasses" @click="handleClick" :disabled="disabled" v-if="!loading">
        {{ buttonText }}
    </button>
</template>

<script>
export default {
    name: 'MainButton',
    props: {
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
            default: false
        },
        type: {
            type: String,
            default: 'black',
            validator: (value) => ['green', 'red', 'yellow', 'blue', 'black', 'gray', 'white'].includes(value)
        }
    },
    computed: {
        computedClasses() {
            const baseClasses = [
                'btn',
                'h-[40px]',
                'text-white',
                'transition-colors',
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
                'cursor-pointer'
            ];

            if (this.disabled) {
                return [...baseClasses, 'bg-gray'];
            } else {
                return [
                ...baseClasses,
                `bg-${this.getBackgroundColor()}`,
                `hover:bg-${this.getHoverBackgroundColor()}`,
                ];
            }
        },
    },
    methods: {
        handleClick() {
            if (!this.disabled && !this.loading) {
                this.click();
            }
        },
        getBackgroundColor() {
            if (this.type !== 'black') {
                return `${this.type}-700`;
            } else if (this.type === 'white') {
                return `gray-100`;
            } else {
                return `${this.type}`;
            }
        },
        getHoverBackgroundColor() {
            if (this.type !== 'black') {
                return `${this.type}-800`;
            } else if (this.type === 'white') {
                return `gray-200`;
            } else {
                return `[#101010]`;
            }
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
