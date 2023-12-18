<template>
    <section id="table" class="flex flex-col items-center justify-start w-full min-h-[calc(100vh-202px)] text-black bg-gray-50 h-auto">
        <div v-if="authStore.loggedIn" class="xs:max-w-screen-[450px] sm:max-w-screen-sm md:max-w-screen-md lg:max-w-screen-lg xl:max-w-screen-xl 2xl:max-w-screen-xl w-full h-full flex flex-col justify-center items-start">
            <div class="flex justify-between items-center w-full h-[70px] mt-2">
                <div class="w-auto px-5 bg-white border-[1px] border-gray-300 rounded-md">
                    <div class="w-auto h-[60px] bg-white pt-1.5">
                        <v-tabs v-if="this.authStore.user.user.user_type === 'admin'" v-model="tab">
                            <v-tab value="1" class="rounded-tl-lg">Zawodnicy</v-tab>
                            <v-tab value="2" class="rounded-tr-lg">Trenerzy</v-tab>
                        </v-tabs>
                        <v-tabs v-else v-model="tab">
                            <v-tab value="1" class="rounded-t-lg">Zawodnicy</v-tab>
                        </v-tabs>
                    </div>
                </div>
                <div class="flex flex-col">
                    <div class="flex flex-row justify-end items-center font-raleway">
                        <span>
                            Całkowita liczba zawodników: 
                        </span>
                        <div v-if="loading" class="skeleton h-[24px] w-[24px] ml-2 rounded-md"></div>
                        <span v-else class="ml-2 font-bold">{{this.players.length}}</span>
                    </div>
                    <div v-if="this.authStore.user.user.user_type === 'admin'" class="flex flex-row justify-end items-center font-raleway">
                        <span>
                            Całkowita liczba trenerów: 
                        </span>
                        <div v-if="loading" class="skeleton h-[24px] w-[24px] ml-2 rounded-md"></div>
                        <span v-else class="ml-2 font-bold">{{this.players.length}}</span>
                    </div>
                </div>
            </div>
            <v-window v-model="tab" class="w-full">
                <v-window-item value="1" class="w-[99%] flex flex-col items-center justify-center">
                    <div class="flex flex-row w-full justify-between items-center my-2 h-[70px]">
                        <div class="flex flex-row justify-start items-center">
                            <span class="text-3xl font-bold font-raleway mr-10">Zawodnicy</span>
                            <button class="btn h-[40px] text-white bg-black hover:bg-[#101010] transition ease-in-out duration-300 font-medium rounded text-sm px-4 py-1 w-auto uppercase flex items-center justify-center">
                                Dodaj zawodnika
                            </button> 
                        </div>
                        <div>
                            <div class="dropdown dropdown-bottom dropdown-end">
                                <button tabindex="0" role="button" class="btn h-[40px] text-white bg-black hover:bg-[#101010] transition ease-in-out duration-300 font-medium rounded text-sm px-4 py-1 w-auto uppercase flex items-center justify-center">Sortuj <v-icon>mdi-arrow-down</v-icon></button>
                                <ul class="dropdown-content z-[1] menu p-2 shadow bg-base-100 rounded-box w-[180px]">
                                    <li>
                                        <div class="form-control">
                                            <label class="label cursor-pointer">
                                                <input v-model="sortingOptions.age" @change="updateSorting" type="checkbox" class="checkbox checkbox-[#000000] bg-gray-300 border-[1px] border-gray-300 mr-2" />
                                                <span class="label-text">Wiek</span> 
                                            </label>
                                        </div>
                                    </li>
                                    <li>
                                        <div class="form-control">
                                            <label class="label cursor-pointer">
                                                <input v-model="sortingOptions.position" @change="updateSorting" type="checkbox" class="checkbox checkbox-[#000000] bg-gray-300 border-[1px] border-gray-300 mr-2" />
                                                <span class="label-text">Pozycja</span> 
                                            </label>
                                        </div>
                                    </li>
                                    <li>
                                        <div class="form-control">
                                            <label class="label cursor-pointer">
                                                <input v-model="sortingOptions.year" @change="updateSorting" type="checkbox" class="checkbox checkbox-[#000000] bg-gray-300 border-[1px] border-gray-300 mr-2" />
                                                <span class="label-text">Rocznik</span> 
                                            </label>
                                        </div>
                                    </li>
                                    <li>
                                        <div class="form-control">
                                            <label class="label cursor-pointer">
                                                <input v-model="sortingOptions.number" @change="updateSorting" type="checkbox" class="checkbox checkbox-[#000000] bg-gray-300 border-[1px] border-gray-300 mr-2" />
                                                <span class="label-text">Numer</span> 
                                            </label>
                                        </div>
                                    </li>
                                </ul>
                            </div>
                        </div>
                    </div>
                    <article class="w-full border-[1px] border-gray-300 bg-white h-[500px] rounded-[6px] shadow-lg">
                        <div v-if="loading" class="w-full h-full bg-gray-200 flex items-center justify-center">
                            <div class="spinner"></div>
                        </div>
                        <div v-else>
                            <div class="w-full h-[50px] border-b-[1px] border-gray-300 flex items-center justify-between px-10 font-inter text-gray-600">
                                <div class="flex items-center justify-center">
                                    <span class="w-[70px] h-full">Photo</span>
                                </div>
                                <div class="flex items-center justify-center">
                                    <span class="w-[150px] h-full">Name</span>
                                </div>
                                <div class="flex items-center justify-center">
                                    <span class="w-[90px] h-full">Pozycja</span>
                                </div>
                                <div class="flex items-center justify-center">
                                    <span class="w-[90px] h-full">Status</span>
                                </div>
                                <div class="flex items-center justify-center">
                                    <span class="w-[70px] h-full">Number</span>
                                </div>
                                <div class="flex items-center justify-center">
                                    <span class="w-[90px] h-full">Year</span>
                                </div>
                                <div class="flex items-center justify-center">
                                    <span class="w-[120px] h-full">Operacje</span>
                                </div>
                            </div>
                            {{ this.playersSorted[this.currentPagePlayers - 1] }}
                            <!-- <div v-for="player in this.players" :key="player.id" class="mb-5">
                                {{ player }}
                            </div> -->
                        </div>
                    </article>
                    <div class="w-full h-auto mt-5 flex text-black items-center justify-center font-raleway">
                        <select @change="this.changeItemsPerPage(this.itemsPerPage)" v-model="this.itemsPerPage" class="py-3 px-4 block w-[200px] bg-white rounded-md text-sm h-[44px]">
                            <option :value="5">5</option>
                            <option :value="6">6</option>
                        </select>
                        {{ itemsPerPage }}
                        <div class="pagination flex items-center justify-center flex-col">
                            <span v-if="this.pagesPlayers > 1" class="flex items-center">
                                <button @click="this.currentPagePlayers = 1" class="text-black w-[35px] h-[35px]">
                                    <v-icon>mdi-chevron-left</v-icon>
                                    <v-icon class="ml-[-18px]">mdi-chevron-left</v-icon>
                                </button>
                                <button @click="this.currentPagePlayers--" :disabled="this.currentPagePlayers === 1" class="text-black w-[35px] h-[35px]">
                                    <v-icon>mdi-chevron-left</v-icon>
                                </button>
                                <div v-for="pageNumber in displayedPages" @click="this.currentPagePlayers = pageNumber" :key="pageNumber" class="bg-white cursor-pointer border-gray-300 border-[1px] w-[35px] h-[35px] mx-1 flex items-center justify-center rounded-md" :class="{ 'current-page-div': this.currentPagePlayers === pageNumber }">
                                    <button :class="{ 'current-page': this.currentPagePlayers === pageNumber }" class="bg-white text-black border-2">
                                        {{ pageNumber }}
                                    </button>
                                </div>
                                <button @click="this.currentPagePlayers++" :disabled="this.currentPagePlayers === this.pagesPlayers" class="text-black w-[35px] h-[35px]">
                                    <v-icon>mdi-chevron-right</v-icon>
                                </button>
                                <button @click="this.currentPagePlayers = this.pagesPlayers" class="text-black w-[35px] h-[35px]">
                                    <v-icon>mdi-chevron-right</v-icon>
                                    <v-icon class="ml-[-18px]">mdi-chevron-right</v-icon>
                                </button>
                            </span>
                            <span class="mt-2">
                                Strona <b>{{ this.currentPagePlayers }}</b> z <b>{{ this.pagesPlayers }}</b>
                            </span>
                        </div>
                    </div>
                </v-window-item>
                
                <v-window-item value="2">
                    <div class="flex flex-row w-full justify-between items-center my-2 h-[70px]">
                        <div class="flex flex-row justify-start items-center">
                            <span class="text-3xl font-bold font-raleway mr-10">Trenerzy</span>
                            <button class="btn h-[40px] text-white bg-black hover:bg-[#101010] transition ease-in-out duration-300 font-medium rounded text-sm px-4 py-1 w-auto uppercase flex items-center justify-center">
                                Dodaj trenera
                            </button> 
                        </div>
                        <div>
                            <div class="dropdown dropdown-bottom dropdown-end">
                                <button tabindex="0" role="button" class="btn h-[40px] text-white bg-black hover:bg-[#101010] transition ease-in-out duration-300 font-medium rounded text-sm px-4 py-1 w-auto uppercase flex items-center justify-center">Sortuj <v-icon>mdi-arrow-down</v-icon></button>
                                <ul class="dropdown-content z-[1] menu p-2 shadow bg-base-100 rounded-box w-[180px]">
                                    <li>
                                        <div class="form-control">
                                            <label class="label cursor-pointer">
                                                <input v-model="sortingOptions.age" @change="updateSorting" type="checkbox" class="checkbox checkbox-[#000000] bg-gray-300 border-[1px] border-gray-300 mr-2" />
                                                <span class="label-text">Wiek</span> 
                                            </label>
                                        </div>
                                    </li>
                                    <li>
                                        <div class="form-control">
                                            <label class="label cursor-pointer">
                                                <input v-model="sortingOptions.position" @change="updateSorting" type="checkbox" class="checkbox checkbox-[#000000] bg-gray-300 border-[1px] border-gray-300 mr-2" />
                                                <span class="label-text">Pozycja</span> 
                                            </label>
                                        </div>
                                    </li>
                                    <li>
                                        <div class="form-control">
                                            <label class="label cursor-pointer">
                                                <input v-model="sortingOptions.year" @change="updateSorting" type="checkbox" class="checkbox checkbox-[#000000] bg-gray-300 border-[1px] border-gray-300 mr-2" />
                                                <span class="label-text">Rocznik</span> 
                                            </label>
                                        </div>
                                    </li>
                                    <li>
                                        <div class="form-control">
                                            <label class="label cursor-pointer">
                                                <input v-model="sortingOptions.number" @change="updateSorting" type="checkbox" class="checkbox checkbox-[#000000] bg-gray-300 border-[1px] border-gray-300 mr-2" />
                                                <span class="label-text">Numer</span> 
                                            </label>
                                        </div>
                                    </li>
                                </ul>
                            </div>
                        </div>
                    </div>
                    <article class="w-full border-[1px] border-gray-300 bg-white h-[500px] rounded-sm">
                        <div v-if="loading" class="w-full h-full bg-gray-200 flex items-center justify-center">
                            <div class="spinner"></div>
                        </div>
                        <div v-else class="py-5 px-8">
                            {{ this.players }}
                            <span>Lorem ipsum dolor sit amet consectetur adipisicing elit. Veniam at corrupti quibusdam quaerat dolorum consectetur sed itaque nobis expedita libero dolor numquam nesciunt repellendus in mollitia eos excepturi deleniti quas, sunt sapiente commodi nihil doloremque perferendis rerum! A recusandae tempore libero eligendi, facere cupiditate quis consequuntur pariatur odio ex minima esse quidem veniam eius, perspiciatis quos, blanditiis fuga itaque quo aperiam illo? Facilis eveniet commodi officiis soluta natus est consectetur eum dolore, ratione adipisci, rerum a nobis quis quaerat maxime, expedita porro odit ea nesciunt esse explicabo harum ipsa assumenda. Adipisci aperiam at itaque. Soluta accusantium necessitatibus officiis inventore laboriosam quasi impedit illum numquam quam perspiciatis incidunt sequi provident neque, qui repellat quas unde autem temporibus voluptatem eligendi culpa, voluptatum eius nobis ut?</span>
                        </div>
                    </article>
                </v-window-item>
            </v-window>
            <span></span>
            
            <div>
                <label for="age">Sort by Age</label>
            <input type="checkbox" id="age" v-model="sortingOptions.age" @change="updateSorting">

            <label for="position">Sort by Position</label>
            <input type="checkbox" id="position" v-model="sortingOptions.position" @change="updateSorting">

            <label for="year">Sort by Year</label>
            <input type="checkbox" id="year" v-model="sortingOptions.year" @change="updateSorting">

                <!-- <button @click="this.sortData(['age', 'position'])" class="mb-10 p-5 bg-gray">sort</button> -->
               
            </div>
        </div>
    </section>
</template>

<script lang="ts">
import { useAuthStore } from '../../stores/auth';
import { getToken } from '../../services/token/getToken';
import { getPlayers } from '../../services/players/players';

export default{
    data() {
        return {
            loadingTest: true,
            authStore: useAuthStore(),
            loading: false,
            sortingOptions: {
                age: false,
                position: false,
                year: false,
                number: false,
            },
            players: [],
            tab: null,
            itemsPerPage: 5,

            pagesPlayers: 0,
            currentPagePlayers: 1,
            playersSorted: [],

            pagesTrainers: 0,
            currentPageTrainers: 1,
            trainersSorted: [],

        }
    },
    async created() {
        if (!this.authStore.loggedIn) {
            this.$router.push('/auth/login?action=login');
        }
        await this.getAllPlayers();
    },
    computed: {
        displayedPages() {
            const maxDisplayed = 5;
            let start;
            let end;

            if (this.pagesPlayers <= maxDisplayed) {
                start = 1;
                end = this.pagesPlayers;
            } else if (this.currentPagePlayers <= Math.floor(maxDisplayed / 2) + 1) {
                start = 1;
                end = maxDisplayed;
            } else if (this.currentPagePlayers >= this.pagesPlayers - Math.floor(maxDisplayed / 2)) {
                start = this.pagesPlayers - maxDisplayed + 1;
                end = this.pagesPlayers;
            } else {
                start = this.currentPagePlayers - Math.floor(maxDisplayed / 2);
                end = start + maxDisplayed - 1;
            }

            return Array.from({ length: end - start + 1 }, (_, i) => i + start);
        }
    },
    methods: {
        async getAllPlayers() {
            try {
                this.loading = true;
                this.players = await getPlayers(); 
                await this.organizePlayers(); 
                this.loading = false;
            } catch (error) {
                console.error(error);
                this.loading = false;
            }
        },
        async organizePlayers() {
            console.log(this.itemsPerPage)
            let playersToSort = [...this.players]; // Create a copy of this.players
            this.pagesPlayers = Math.ceil(playersToSort.length / this.itemsPerPage);
            this.playersSorted = [];
            while (playersToSort.length > 0) {
                this.playersSorted.push(playersToSort.splice(0, this.itemsPerPage));
            }
            console.log(this.playersSorted)
        },
        async changeItemsPerPage(number) {
            this.itemsPerPage = number;
            console.log(this.itemsPerPage)
            await this.organizePlayers();
        },
        async getTokenString() {
            return await getToken()
        },
        updateSorting() {
            const selectedOptions = Object.keys(this.sortingOptions).filter(
                option => this.sortingOptions[option]
            );
            const sortedData = this.sortData(selectedOptions);
        },
        sortData(sortingOptions) {
            const sortingFunctions = {
                age: (a, b) => a.age - b.age,
                position: (a, b) => {
                    const positionsOrder = { BR: 0, OB: 1, PO: 2, NA: 3 };
                    return positionsOrder[a.position] - positionsOrder[b.position];
                },
                year: (a, b) => a.year - b.year,
                number: (a, b) => a.number - b.number,
            };
            
            const sortFunction = (a, b) => {
                for (const option of sortingOptions) {
                    const result = sortingFunctions[option](a, b);
                    if (result !== 0) {
                        return result;
                    }
                }
                return 0;
            };

            const sortedArray = [...this.players].sort(sortFunction);
            this.players = sortedArray;
        }
    }
};
</script>

<style lang="scss" scoped>
@keyframes spin {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}

// Spinner class
.spinner {
  border: 4px solid white;
  border-top: 4px solid black;
  border-radius: 50%;
  width: 50px;
  height: 50px;
  animation: spin 1s linear infinite;
}

.current-page {
    font-weight: bold; 
}

.current-page-div {
    border: 1px solid black !important;
}
</style>