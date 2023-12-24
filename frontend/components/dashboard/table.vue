<template>
    <section id="table" class="flex flex-col items-center justify-start w-full min-h-[calc(100vh-110px)] text-black bg-[#f5f5f5] dark:bg-slate-800 h-auto">
        <div v-if="authStore.loggedIn" class="xs:max-w-screen-[450px] sm:max-w-screen-sm md:max-w-screen-md lg:max-w-screen-lg xl:max-w-screen-xl 2xl:max-w-screen-xl w-full h-full flex flex-col justify-center items-center">
            <div class="flex justify-between items-center w-full h-[70px] mt-5">
                <div class="rounded-[0.5rem] w-full flex justify-between">
                    <div class="w-auto h-[48px] bg-white font-inter rounded-[0.5rem]">
                        <v-tabs v-if="this.authStore.user.user.user_type === 'admin'" v-model="tab" class="flex items-center justify-center">
                            <v-tab value="1" class="rounded-tl-lg ml-5 mt-[-3px]">Zawodnicy</v-tab>
                            <v-tab value="2" class="rounded-tr-lg mr-5 mt-[-3px]">Trenerzy</v-tab>
                        </v-tabs>
                        <v-tabs v-else v-model="tab">
                            <v-tab value="1" class="rounded-t-lg">Zawodnicy</v-tab>
                        </v-tabs>
                    </div>
                    <div class="bg-white w-auto h-[48px] rounded-[0.5rem] ml-5">
                        <div class="relative h-[48px] flex items-center justify-center">
                            <span class="absolute inset-y-0 left-0 flex items-center pl-3">
                                <v-icon>mdi-magnify</v-icon>
                            </span>
                            <input v-model="searchText" type="text" class="h-full pl-10 pr-4 py-2 rounded-[0.5rem] block w-full font-inter text-[1rem] leading-[1.5] tracking-[0.005em]" placeholder="Szukaj zawodnika...">
                            <span v-if="searchText.length > 0" @click="searchText = ''" class="absolute inset-y-0 right-0 flex items-center pr-3 cursor-pointer">
                                <v-icon>mdi-close</v-icon>
                            </span>
                        </div>
                    </div>
                </div>
            </div>
            <v-window v-model="tab" class="w-full">
                <v-window-item value="1" class="w-full flex flex-col items-center justify-center">
                    <div class="flex flex-row h-[70px] mb-2 justify-between w-full items-center">
                        <div class="w-full h-[48px] flex justify-between">
                            <MainButton :click="addPlayer" type="green" :disabled="false" />
                            <div class="flex">
                                <div v-if="shouldDisplayFilterDiv" class="flex flex-col font-inter mr-3 items-end justify-center">
                                    <span class="text-[1rem]">Filtrowanie:</span>
                                    <div class="flex flex-row">
                                        <span v-for="(key, i) in Object.keys(this.filterOptions)" :key="i" class="text-[0.825rem] text-gray-500 flex flex-row">
                                            <span v-if="this.filterOptions[key] === true" class="flex ml-1"><v-icon @click="this.filterOptions[key] = false, updateFilter(), this.searchText = ''" class="cursor-pointer">mdi-close</v-icon>{{ this.filterOptionsTranslations[i] }}</span>
                                        </span>
                                    </div>
                                </div>
                                <MainButton :click="filter" type="black" buttonText="Filtruj..." class="mr-5" />
                                <div class="dropdown dropdown-bottom dropdown-end">
                                    <MainButton tabindex="0" type="black" buttonText="Sortuj" />
                                    <ul class="dropdown-content z-[1] menu p-2 shadow bg-white border-[1px] border-gray-300 rounded-box w-[180px] mt-2">
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
                                        <li>
                                            <div class="form-control">
                                                <label class="label cursor-pointer">
                                                    <input v-model="sortingOptions.status" @change="updateSorting" type="checkbox" class="checkbox checkbox-[#000000] bg-gray-300 border-[1px] border-gray-300 mr-2" />
                                                    <span class="label-text">Status</span> 
                                                </label>
                                            </div>
                                        </li>
                                    </ul>
                                </div>
                                <v-icon @click="changePlayersDirection()" class="text-white bg-black h-[48px] w-[48px] hover:bg-[#101010] transition ease-in-out duration-300 font-medium rounded-[0.5rem] text-[1rem] ml-5 flex items-center justify-center leading-[1.5] tracking-[0.005em] cursor-pointer">mdi-arrow-up-down</v-icon>
                            </div>
                        </div>
                    </div>
                    <article class="w-full rounded-[0.5rem] bg-white h-auto">
                        <div v-if="loading" class="w-full min-h-[660px] h-full flex items-center justify-center">
                            <div class="spinner"></div>
                        </div>
                        <div v-else class="w-full flex items-center justify-start flex-col min-h-[660px]">
                            <div class="w-full h-[60px] border-b-[1px] border-gray-200 flex items-center justify-between px-10 font-inter text-[#0f0f0f] text-[1rem] font-medium leading-6 tracking-[0.005em]">
                                <div class="flex items-center justify-center">
                                    <span class="w-[60px] h-full">Photo</span>
                                </div>
                                <div class="flex items-center justify-center">
                                    <span class="w-[150px] h-full">Name</span>
                                </div>
                                <div class="flex items-center justify-center">
                                    <span class="w-[90px] h-full">Pozycja</span>
                                </div>
                                <div class="flex items-center justify-center">
                                    <span class="w-[120px] h-full">Status</span>
                                </div>
                                <div class="flex items-center justify-center text-center">
                                    <span class="w-[70px] h-full">Number</span>
                                </div>
                                <div class="flex items-center justify-center text-center">
                                    <span class="w-[90px] h-full">Year</span>
                                </div>
                                <div v-if="this.authStore.user.user.user_type === 'admin'" class="flex items-center justify-center text-center">
                                    <span class="w-[120px] h-full">Operacje</span>
                                </div>
                            </div>
                            <div v-if="this.playersSorted.length === 0" class="w-full h-[599px] border-b-[0.0625rem] border-[hsl(0 0% 92%)] flex items-center justify-center px-10 font-inter text-[#2b2b2b]">
                                <span class="font-inter text-[3rem]">
                                    Nic nie znaleziono!
                                </span>
                            </div>
                            <div v-for="(player, index) in this.playersSorted[this.currentPagePlayers - 1]" :key="player.id" :class="{ 'border-b-[0.0625rem] border-[hsl(0 0% 92%)]': index !== this.playersSorted[this.currentPagePlayers - 1].length - 1 }" class="w-full h-[60px] flex items-center justify-between px-10 font-inter text-[#2b2b2b]">
                                <div class="flex items-center justify-start w-[60px]">
                                    <img :src="player.image" :alt="player.name" class="w-[50px] h-[50px] rounded-md">
                                </div>
                                <div class="flex items-center justify-center">
                                    <span class="w-[150px] h-full">{{player.name}}</span>
                                </div>
                                <div class="flex items-center justify-center">
                                    <span v-if="player.position.value === 'BR'" class="w-[90px] h-full">Bramkarz</span>
                                    <span v-if="player.position.value === 'OB'" class="w-[90px] h-full">Obrońca</span>
                                    <span v-if="player.position.value === 'PO'" class="w-[90px] h-full">Pomocnik</span>
                                    <span v-if="player.position.value === 'NA'" class="w-[90px] h-full">Napastnik</span>
                                </div>
                                <div class="flex items-center justify-center text-center">
                                    <span v-if="player.status.value === 'nieaktywny'" class="h-full border-[1px] border-red-600 bg-red-50 text-red text-sm rounded-full w-[120px] py-1">Nieaktywny</span>
                                    <span v-else class="h-full border-[1px] border-green-600 bg-green-50 text-green text-sm rounded-full w-[120px] py-1">Aktywny</span>
                                </div>
                                <div class="flex items-center justify-center text-center">
                                    <span class="w-[70px] h-full">{{player.number}}</span>
                                </div>
                                <div class="flex items-center justify-center text-center">
                                    <span class="w-[90px] h-full">{{player.year}}</span>
                                </div>
                                <div v-if="this.authStore.user.user.user_type === 'admin'" class="flex items-center justify-center w-[120px]">
                                    <v-icon @click="this.updatePlayer(player.id, player.name, player.position, player.status, player.number, player.year)">mdi-pencil-plus</v-icon>
                                    <v-icon @click="this.imagePlayer(player.id, player.name, player.image)" class="mx-5">mdi-image-edit</v-icon>
                                    <v-icon @click="this.deletePlayer(player.id, player.name)">mdi-delete</v-icon>
                                </div>
                            </div>
                        </div>
                    </article>
                    <div v-if="!loading && pagesPlayers > 0" class="w-full h-auto my-5 flex text-black items-center justify-between font-inter">
                        <div class="w-[230px] h-full bg-white rounded-md flex items-center">
                            <select @change="this.changeItemsPerPage(this.itemsPerPage)" v-model="this.itemsPerPage" class="py-3 px-4 block w-[88px] bg-white rounded-[0.5rem] text-sm h-[44px]">
                                <option :value="10">10</option>
                                <option :value="20">20</option>
                                <option :value="50">50</option>
                            </select>
                            <span class="text-sm border-l-[1px] h-full pl-2">Wyniki na stronie</span>
                        </div>
                        <div class="pagination flex items-center justify-center flex-col">
                            <span v-if="this.pagesPlayers > 1" class="flex items-center">
                                <button @click="this.currentPagePlayers = 1" class="text-black w-[35px] h-[35px] cursor-pointer">
                                    <v-icon>mdi-chevron-left</v-icon>
                                    <v-icon class="ml-[-18px]">mdi-chevron-left</v-icon>
                                </button>
                                <button @click="this.currentPagePlayers--" :disabled="this.currentPagePlayers === 1" class="text-black w-[35px] h-[35px] cursor-pointer">
                                    <v-icon>mdi-chevron-left</v-icon>
                                </button>
                                <div v-for="pageNumber in displayedPages" @click="this.currentPagePlayers = pageNumber" :key="pageNumber" class="bg-white w-[35px] h-[35px] mx-1 flex items-center justify-center rounded-md cursor-pointer" :class="{ 'current-page-div': this.currentPagePlayers === pageNumber }">
                                    <button :class="{ 'current-page': this.currentPagePlayers === pageNumber }" class="bg-white text-black border-2">
                                        {{ pageNumber }}
                                    </button>
                                </div>
                                <button @click="this.currentPagePlayers++" :disabled="this.currentPagePlayers === this.pagesPlayers" class="text-black w-[35px] h-[35px] cursor-pointer">
                                    <v-icon>mdi-chevron-right</v-icon>
                                </button>
                                <button @click="this.currentPagePlayers = this.pagesPlayers" class="text-black w-[35px] h-[35px] cursor-pointer">
                                    <v-icon>mdi-chevron-right</v-icon>
                                    <v-icon class="ml-[-18px]">mdi-chevron-right</v-icon>
                                </button>
                            </span>
                            <span class="mt-2">
                                Strona <b>{{ this.currentPagePlayers }}</b> z <b>{{ this.pagesPlayers }}</b>
                            </span>
                        </div>
                        <div class="w-[230px] h-full flex items-center justify-end">
                            <span class="font-bold">{{ this.playersSorted[this.currentPagePlayers - 1].length }}</span>
                            <span class="mx-1">z</span>
                            <span class="font-bold">{{ this.players.length }}</span>
                        </div>
                    </div>
                </v-window-item>
                
                <v-window-item value="2">
                    <div class="flex flex-row w-full justify-between items-center my-2 h-[70px]">
                        <div class="flex flex-row justify-start items-center">
                            <span class="text-3xl font-bold font-inter mr-10">Trenerzy</span>
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
                                    <li>
                                        <div class="form-control">
                                            <label class="label cursor-pointer">
                                                <input v-model="sortingOptions.status" @change="updateSorting" type="checkbox" class="checkbox checkbox-[#000000] bg-gray-300 border-[1px] border-gray-300 mr-2" />
                                                <span class="label-text">Status</span> 
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
            <v-dialog v-model="dialogUpdate" persistent transition="dialog-bottom-transition">
                <v-form @submit.prevent ref="updateValid" v-model="updateValid" class="bg-white h-auto w-[500px] p-10 rounded-[1rem] border-[1px] border-gray-300 shadow-md">
                    <div class="flex flex-row justify-between items-start w-full mb-6">
                        <div class="bg-gray-300 h-[50px] w-[50px] rounded-full flex items-center justify-center">
                            <v-icon>mdi-pencil-plus</v-icon>
                        </div>
                        <v-icon @click="this.dialogUpdate = false; this.currentUpdate = {};" class="cursor-pointer text-gray-500 transition ease-in-out duration-300" style="font-size:28px !important;">mdi-close</v-icon>
                    </div>
                    <div class="flex flex-col mb-10 font-poppins">
                        <span class="font-medium mb-1 text-[1.5rem] leading-[1.5] tracking-[0.005em]">Edycja danych zawodnika.</span>
                        <span class="text-[1rem] text-gray-500 leading-[1.5] tracking-[0.005em] mb-3">Historię edycji tego zawodnika możesz sprawdzić w <NuxtLink :to="`/app/user-history?id=${this.currentUpdate.id}`" class="font-bold text-black">Jego historii</NuxtLink>.</span>
                    </div>
                    <div class="flex flex-col mt-3 mb-8 font-poppins">
                        <v-text-field v-model="this.currentUpdate.name" :rules="this.nameRules" variant="outlined" class="max-h-[56px] w-full mb-8" placeholder="Name" label="Name"></v-text-field>
                        <div class="flex flex-row justify-between mb-8">
                            <v-text-field v-model="this.currentUpdate.number" :rules="this.numberRules" variant="outlined" class="max-h-[56px] max-w-[48%]" placeholder="Number" label="Number"></v-text-field>
                            <v-text-field v-model="this.currentUpdate.year" :rules="this.yearRules" variant="outlined" class="max-h-[56px] max-w-[48%]" placeholder="Birth year" label="Birth year"></v-text-field>
                        </div>
                        <div class="flex flex-row justify-between">
                            <v-select v-model="this.currentUpdate.status" variant="outlined" class="max-h-[56px] max-w-[48%]" :items="statuses" item-title="title" item-value="value" return-object placeholder="Status" label="Status"></v-select>
                            <v-select v-model="this.currentUpdate.position" variant="outlined" class="max-h-[56px] max-w-[48%]" :items="positions" item-title="title" item-value="value" return-object placeholder="Position" label="Position"></v-select>
                        </div>
                    </div>
                    <div class="flex flex-row w-full items-center justify-end font-poppins">
                        <MainButton :click="updatePlayerClose" type="white" buttonText="Anuluj" style="color: black !important;" />
                        <MainButton :click="updatePlayerDialog" type="black" :loading="buttonLoading" :disabled="!updateValid" buttonText="Zapisz" class="ml-5" />
                    </div>
                </v-form>
            </v-dialog>
            <v-dialog v-model="dialogImage" persistent transition="dialog-bottom-transition">
                <div class="bg-white h-auto w-[500px] p-10 rounded-lg border-[1px] border-gray-300 shadow-md">
                    <div class="flex flex-row justify-between items-start w-full mb-6">
                        <div class="bg-blue-300 h-[50px] w-[50px] rounded-full flex items-center justify-center">
                            <v-icon class="text-blue-700">mdi-image-edit</v-icon>
                        </div>
                        <v-icon @click="this.dialogImage = false; this.currentImage = {}; this.selectedImage = {};" class="cursor-pointer text-gray-500 transition ease-in-out duration-300" style="font-size:28px !important;">mdi-close</v-icon>
                    </div>
                    <div class="flex flex-col mb-10 font-poppins">
                        <span class="font-medium mb-1 text-[1.5rem] leading-[1.5] tracking-[0.005em]">Edycja zdjęcia zawodnika.</span>
                        <span class="text-[1rem] text-gray-500 leading-[1.5] tracking-[0.005em] mb-3">Dodajesz nowe zdjęcie zawodnika <b>{{ this.currentImage.name }}</b>.</span>
                        <span class="text-[1rem] text-red-700 leading-[1.5] tracking-[0.005em]">Ta akcja <b>nie może</b> być cofnięta.</span>
                    </div>

                    <div v-if="currentImage.image !== null && isObjectEmpty(selectedImage)" class="flex flex-col mt-3 mb-8 font-inter">
                        <span class="font-medium text-[1.25rem] leading-[1.5] tracking-[0.005em] mb-3">Obecne zdjęcie</span>
                        <img :src="currentImage.image" :alt="currentImage.name" class="rounded-xl">
                    </div>

                    <div v-else class="flex flex-col mt-3 font-inter">
                        <span v-if="isObjectEmpty(selectedImage)" class="italic mb-10">Zawodnik obecnie nie ma zdjęcia.</span>

                        <div v-if="!isObjectEmpty(selectedImage)" class="flex flex-row justify-between w-full items-center">
                            <span class="font-medium text-[1.25rem] leading-[1.5] tracking-[0.005em] mb-3">Dodane zdjęcie</span>
                            <v-icon @click="this.selectedImage = {};this.imageIsCropped = null;" class="cursor-pointer">mdi-close</v-icon>
                        </div>

                        <cropper v-if="!isObjectEmpty(selectedImage) && !this.imageIsCropped" class="cropper" :src="selectedImage.url" :stencil-props="{aspectRatio: 1 / 1, }" ref="cropper"/>
                        <div v-if="!isObjectEmpty(selectedImage) && !this.imageIsCropped" class="flex mt-5 w-full items-center justify-end">
                            <MainButton :click="imagePlayerClose" type="white" buttonText="Anuluj" style="color: black !important;" />
                            <MainButton :click="deleteImagePreview" type="red" buttonText="Usuń zdjęcie" class="ml-5" />
                            <MainButton :click="cropImage" type="green" buttonText="Wytnij" class="ml-5" />
                        </div>

                        <canvas v-if="!isObjectEmpty(selectedImage) && this.imageIsCropped" ref="canvas" class="rounded-xl max-h-[600px] w-auto object-contain"></canvas>
                    </div>

                    <div v-if="isObjectEmpty(selectedImage)" class="flex flex-row w-full items-center justify-end font-poppins">
                        <MainButton :click="imagePlayerClose" type="white" buttonText="Anuluj" style="color: black !important;" />
                        <label v-if="isObjectEmpty(selectedImage)" @click="this.loadingImage = true;" for="file-upload" class="btn h-[40px] text-white bg-blue-700 hover:bg-blue-800 transition ease-in-out duration-300 rounded-[0.5rem] text-[1rem] font-medium px-4 py-1 w-auto flex items-center justify-center font-inter leading-[1.5] tracking-[0.005em] ml-5">
                            Dodaj nowe zdjęcie
                        </label>
                        <input type="file" id="file-upload" ref="fileInput" accept="image/*" @change="previewImage">
                    </div>

                    <div v-if="imageIsCropped && !isObjectEmpty(selectedImage)" class="flex flex-row items-center justify-end mt-10">
                        <MainButton :click="imagePlayerClose" type="white" buttonText="Anuluj" style="color: black !important;" />
                        <MainButton v-if="croppedImage !== null" :click="deleteCanvasImage" type="red" buttonText="Usuń zdjęcie" class="ml-5" />
                        <Input :icon="false" :click="imagePlayerDialog" buttonText="Zapisz zdjęcie" class="ml-5" />
                    </div>
                </div>
            </v-dialog>
            <v-dialog v-model="dialogDelete" persistent transition="dialog-bottom-transition">
                <v-form @submit.prevent ref="deleteValid" v-model="deleteValid"  class="bg-white h-auto w-[500px] p-10 rounded-lg border-[1px] border-gray-300 shadow-md">
                    <div class="flex flex-row justify-between items-start w-full mb-6">
                        <div class="bg-red-200 h-[50px] w-[50px] rounded-full flex items-center justify-center">
                            <v-icon class="text-red-700">mdi-delete</v-icon>
                        </div>
                        <v-icon @click="this.dialogDelete = false; this.currentDelete = {};" class="cursor-pointer text-gray-500 transition ease-in-out duration-300" style="font-size:28px !important;">mdi-close</v-icon>
                    </div>
                    <div class="flex flex-col mb-10 font-poppins">
                        <span class="font-medium mb-1 text-[1.5rem] leading-[1.5] tracking-[0.005em]">Usuwanie zawodnika.</span>
                        <span class="text-[1rem] text-gray-500 leading-[1.5] tracking-[0.005em] mb-3">Czy na pewno chcesz usunąć zawdonika <b>{{ this.currentDelete.name }}</b> z bazy danych?</span>
                        <span class="text-[1rem] text-red-700 leading-[1.5] tracking-[0.005em]">Ta akcja <b>nie może</b> być cofnięta.</span>
                    </div>
                    <div class="flex flex-row w-full items-center justify-end font-poppins">
                        <MainButton :click="deletePlayerClose" type="white" buttonText="Anuluj" style="color: black !important;" />
                        <MainButton :click="deletePlayerDialog" type="red" buttonText="Usuń zawodnika" class="ml-5" />
                    </div>
                </v-form>
            </v-dialog>
            <v-dialog v-model="dialogAdd" persistent transition="dialog-top-transition">
                <v-form @submit.prevent ref="addValid" v-model="addValid" class="bg-white h-auto w-[500px] p-10 rounded-lg border-[1px] border-gray-300 shadow-md">
                    <div class="flex flex-row justify-between items-start w-full mb-6">
                        <div class="bg-green-200 h-[50px] w-[50px] rounded-full flex items-center justify-center">
                            <v-icon class="text-green-700">mdi-account-plus</v-icon>
                        </div>
                        <v-icon @click="this.dialogAdd = false; this.currentAdd = {};" class="cursor-pointer text-gray-500 transition ease-in-out duration-300" style="font-size:28px !important;">mdi-close</v-icon>
                    </div>
                    <div class="flex flex-col mb-10 font-poppins">
                        <span class="font-medium mb-1 text-[1.5rem] leading-[1.5] tracking-[0.005em]">Dodawanie zawodnika.</span>
                        <span class="text-[1rem] text-gray-500 leading-[1.5] tracking-[0.005em]">Dodajesz zawodnika do bazy danych <b>Latarnika Choczewo</b>.</span>
                    </div>
                    <div class="flex flex-col mt-3 mb-8 font-poppins">
                        <v-text-field v-model="this.currentAdd.name" :rules="this.nameRules" variant="outlined" class="max-h-[56px] w-full mb-8" placeholder="Name" label="Name"></v-text-field>
                        <div class="flex flex-row justify-between mb-8">
                            <v-text-field v-model="this.currentAdd.number" :rules="this.numberRules" variant="outlined" class="max-h-[56px] max-w-[48%]" placeholder="Number" label="Number"></v-text-field>
                            <v-text-field v-model="this.currentAdd.year" :rules="this.yearRules" variant="outlined" class="max-h-[56px] max-w-[48%]" placeholder="Birth year" label="Birth year"></v-text-field>
                        </div>
                        <div class="flex flex-row justify-between">
                            <v-select v-model="this.currentAdd.status" variant="outlined" class="max-h-[56px] max-w-[48%]" :items="statuses" item-title="title" item-value="value" return-object placeholder="Status" label="Status"></v-select>
                            <v-select v-model="this.currentAdd.position" variant="outlined" class="max-h-[56px] max-w-[48%]" :items="positions" item-title="title" item-value="value" return-object placeholder="Position" label="Position"></v-select>
                        </div>
                    </div>
                    <div class="flex flex-row w-full items-center justify-end font-inter">
                        <MainButton :click="addPlayerClose" type="white" buttonText="Anuluj" style="color: black !important;" />
                        <MainButton :click="addPlayerDialog" :loading="buttonLoading" :disabled="!addValid" type="green" class="ml-5" />
                    </div>
                </v-form>
            </v-dialog>
            <v-dialog v-model="dialogFilter" persistent transition="dialog-top-transition">
                <div class="bg-white h-auto w-[500px] p-10 rounded-lg border-[1px] border-gray-300 shadow-md">
                    <div class="flex flex-row justify-between items-start w-full mb-6">
                        <div class="bg-yellow-200 h-[50px] w-[50px] rounded-full flex items-center justify-center">
                            <v-icon class="text-yellow-700">mdi-filter</v-icon>
                        </div>
                        <v-icon @click="this.dialogFilter = false;" class="cursor-pointer text-gray-500 transition ease-in-out duration-300" style="font-size:28px !important;">mdi-close</v-icon>
                    </div>
                    <div class="flex flex-col mb-10 font-inter">
                        <span class="font-medium mb-1 text-[1.5rem] leading-[1.5] tracking-[0.005em]">Filtrowanie zawodników.</span>
                        <span class="text-[1rem] text-gray-500 leading-[1.5] tracking-[0.005em]">Wybierz opcje, według których mają być zwróceni zawodnicy.</span>
                    </div>
                    <div class="flex flex-col mt-3 mb-8 font-poppins">
                        <div class="w-full flex items-center">
                            <v-icon class="mr-3">mdi-account-badge</v-icon>
                            <span class="text-[1rem]">Status</span>
                        </div>
                        <div class="flex flex-wrap ml-5 mt-2 font-inter text-black">
                            <div class="form-control w-1/2">
                                <label class="label cursor-pointer flex justify-start">
                                    <input v-if="this.filterOptions.statusN" v-model="filterOptions.statusA" disabled type="checkbox" class="checkbox checkbox-[#000000] bg-gray-300 border-[1px] border-gray-300 mr-2" />
                                    <input v-else v-model="filterOptions.statusA" type="checkbox" class="checkbox checkbox-[#000000] bg-gray-300 border-[1px] border-gray-300 mr-2" />
                                    <span class="label-text">Aktywny</span> 
                                </label>
                            </div>
                            <div class="form-control w-1/2">
                                <label class="label cursor-pointer flex justify-start">
                                    <input v-if="this.filterOptions.statusA" v-model="filterOptions.statusN" disabled type="checkbox" class="checkbox checkbox-[#000000] bg-gray-300 border-[1px] border-gray-300 mr-2" />
                                    <input v-else v-model="filterOptions.statusN" type="checkbox" class="checkbox checkbox-[#000000] bg-gray-300 border-[1px] border-gray-300 mr-2" />
                                    <span class="label-text">Nieaktywny</span> 
                                </label>
                            </div>
                        </div>
                        <hr class="w-full h-[0.0625rem] bg-[hsl(0 0% 92%)] my-2">
                        <div class="w-full flex items-center">
                            <v-icon class="mr-3">mdi-soccer-field</v-icon>
                            <span class="text-[1rem]">Pozycja</span>
                        </div>
                        <div class="flex flex-wrap ml-5 mt-2 font-inter text-black">
                            <div class="form-control w-1/2">
                                <label class="label cursor-pointer flex justify-start">
                                    <input v-if="this.filterOptions.positionO || this.filterOptions.positionP || this.filterOptions.positionN" v-model="filterOptions.positionB" disabled type="checkbox" class="checkbox checkbox-[#000000] bg-gray-300 border-[1px] border-gray-300 mr-2" />
                                    <input v-else v-model="filterOptions.positionB" type="checkbox" class="checkbox checkbox-[#000000] bg-gray-300 border-[1px] border-gray-300 mr-2" />
                                    <span class="label-text">Bramkarz</span> 
                                </label>
                            </div>
                            <div class="form-control w-1/2">
                                <label class="label cursor-pointer flex justify-start">
                                    <input v-if="this.filterOptions.positionB || this.filterOptions.positionP || this.filterOptions.positionN" v-model="filterOptions.positionO" disabled type="checkbox" class="checkbox checkbox-[#000000] bg-gray-300 border-[1px] border-gray-300 mr-2" />
                                    <input v-else v-model="filterOptions.positionO" type="checkbox" class="checkbox checkbox-[#000000] bg-gray-300 border-[1px] border-gray-300 mr-2" />
                                    <span class="label-text">Obrońca</span> 
                                </label>
                            </div>
                            <div class="form-control w-1/2">
                                <label class="label cursor-pointer flex justify-start">
                                    <input v-if="this.filterOptions.positionO || this.filterOptions.positionB || this.filterOptions.positionN" v-model="filterOptions.positionP" disabled type="checkbox" class="checkbox checkbox-[#000000] bg-gray-300 border-[1px] border-gray-300 mr-2" />
                                    <input v-else v-model="filterOptions.positionP" type="checkbox" class="checkbox checkbox-[#000000] bg-gray-300 border-[1px] border-gray-300 mr-2" />
                                    <span class="label-text">Pomocnik</span> 
                                </label>
                            </div>
                            <div class="form-control w-1/2">
                                <label class="label cursor-pointer flex justify-start">
                                    <input v-if="this.filterOptions.positionO || this.filterOptions.positionP || this.filterOptions.positionB" v-model="filterOptions.positionB" disabled type="checkbox" class="checkbox checkbox-[#000000] bg-gray-300 border-[1px] border-gray-300 mr-2" />
                                    <input v-else v-model="filterOptions.positionN" type="checkbox" class="checkbox checkbox-[#000000] bg-gray-300 border-[1px] border-gray-300 mr-2" />
                                    <span class="label-text">Napastnik</span> 
                                </label>
                            </div>
                        </div>
                        <hr class="w-full h-[0.0625rem] bg-[hsl(0 0% 92%)] my-2">
                        <div class="w-full flex items-center">
                            <v-icon class="mr-3">mdi-cake</v-icon>
                            <span class="text-[1rem]">Rocznik</span>
                        </div>
                        <div class="flex flex-wrap ml-5 mt-2 font-inter text-black">
                            <div class="form-control w-1/2">
                                <label class="label cursor-pointer flex justify-start">
                                    <input v-if="this.filterOptions.year2 || this.filterOptions.year3 || this.filterOptions.year4" v-model="filterOptions.year1" type="checkbox" disabled class="checkbox checkbox-[#000000] bg-gray-300 border-[1px] border-gray-300 mr-2" />
                                    <input v-else v-model="filterOptions.year1" type="checkbox" class="checkbox checkbox-[#000000] bg-gray-300 border-[1px] border-gray-300 mr-2" />
                                    <span class="label-text">1970-1999</span> 
                                </label>
                            </div>
                            <div class="form-control w-1/2">
                                <label class="label cursor-pointer flex justify-start">
                                    <input v-if="this.filterOptions.year1 || this.filterOptions.year3 || this.filterOptions.year4" v-model="filterOptions.year2" type="checkbox" disabled class="checkbox checkbox-[#000000] bg-gray-300 border-[1px] border-gray-300 mr-2" />
                                    <input v-else v-model="filterOptions.year2" type="checkbox" class="checkbox checkbox-[#000000] bg-gray-300 border-[1px] border-gray-300 mr-2" />
                                    <span class="label-text">2000-2005</span> 
                                </label>
                            </div>
                            <div class="form-control w-1/2">
                                <label class="label cursor-pointer flex justify-start">
                                    <input v-if="this.filterOptions.year2 || this.filterOptions.year1 || this.filterOptions.year4" v-model="filterOptions.year3" type="checkbox" disabled class="checkbox checkbox-[#000000] bg-gray-300 border-[1px] border-gray-300 mr-2" />
                                    <input v-else v-model="filterOptions.year3" type="checkbox" class="checkbox checkbox-[#000000] bg-gray-300 border-[1px] border-gray-300 mr-2" />
                                    <span class="label-text">2006-2010</span> 
                                </label>
                            </div>
                            <div class="form-control w-1/2">
                                <label class="label cursor-pointer flex justify-start">
                                    <input v-if="this.filterOptions.year2 || this.filterOptions.year3 || this.filterOptions.year1" v-model="filterOptions.year4" type="checkbox" disabled class="checkbox checkbox-[#000000] bg-gray-300 border-[1px] border-gray-300 mr-2" />
                                    <input v-else v-model="filterOptions.year4" type="checkbox" class="checkbox checkbox-[#000000] bg-gray-300 border-[1px] border-gray-300 mr-2" />
                                    <span class="label-text">2010-2019</span> 
                                </label>
                            </div>
                        </div>
                    </div>
                    <div class="flex flex-row w-full items-center justify-end font-poppins">
                        <MainButton :click="filterClose" type="white" buttonText="Anuluj" style="color: black !important;" />
                        <MainButton :click="updateFilter" type="yellow" buttonText="Filtruj" class="ml-5" style="color: white !important;" />
                    </div>
                </div>
            </v-dialog>
        </div>
        <v-snackbar v-model="snackbar" :timeout="snackbarTimeout" variant="outlined" color="rgba(1, 1, 1, 0)">
            <div class="p-4 my-4 w-[350px] text-sm text-green-600 border-[1px] border-green-900 rounded-lg bg-green-50 text-center flex items-start justify-between" role="alert">
                <span class="font-medium font-inter">{{ this.languageStore.t.auth_sign_up_mess_success }}</span> 
                <v-icon @click="this.snackbar = false;">mdi-close</v-icon>
            </div>
        </v-snackbar>
        <v-snackbar v-model="snackbarError" :timeout="snackbarTimeout" variant="outlined" color="rgba(1, 1, 1, 0)">
            <div class="p-4 my-4 w-[350px] text-sm text-red-600 border-[1px] border-red-900 rounded-lg bg-red-50 text-center" role="alert">
                <span class="font-medium font-inter">{{ this.languageStore.t.auth_login_mess_error }}</span> 
                <v-icon @click="this.snackbarError = false;">mdi-close</v-icon>
            </div>
        </v-snackbar>
        <v-snackbar v-model="snackbarErrorPhoto" :timeout="snackbarTimeout" variant="outlined" color="rgba(1, 1, 1, 0)">
            <div class="p-4 my-4 w-[350px] text-sm text-red-600 border-[1px] border-red-900 rounded-lg bg-red-50 text-center" role="alert">
                <span class="font-medium font-inter">{{ this.languageStore.t.auth_login_mess_error }}</span> 
                <v-icon @click="this.snackbarErrorPhoto = false;">mdi-close</v-icon>
            </div>
        </v-snackbar>
    </section>
</template>

<script lang="ts">
import { useAuthStore } from '../../stores/auth';
import { useLanguageStore } from '../../stores/translations';
import { getToken } from '../../services/token/getToken';
import { getPlayers, updatePlayer, createPlayer, deletePlayer } from '../../services/players/players';

import MainButton from '../elements/MainButton.vue'
import Input from '../elements/Input.vue'

import { Cropper } from 'vue-advanced-cropper';
import 'vue-advanced-cropper/dist/style.css'; 

import axios from 'axios';

interface Player {
    id: string;
    name: string;
    position: { title: string; value: string };
    status: { title: string; value: string };
    image: string;
    number: string;
    year: string;
}

interface SelectedImage {
    name: string;
    url: string;
}

interface ApiResponse {
    status: number;
}

export default{
    components: {
        Cropper,
        MainButton,
        Input
    },
    data() {
        return {
            loadingTest: true,
            authStore: useAuthStore(),
            languageStore: useLanguageStore(),
            loading: false,
            loadingImage: false,
            buttonLoading: false,

            sortingOptions: {
                age: false,
                position: false,
                year: false,
                number: false,
                status: false,
            },

            filterOptions: {
                statusA: false,
                statusN: false,
                positionB: false,
                positionO: false,
                positionP: false,
                positionN: false,
                year1: false,
                year2: false,
                year3: false,
                year4: false,
            },
            filterOptionsTranslations: [
                'Aktywny', 'Nieaktywny', 'Bramkarz', 'Obrońca', 'Pomocnik', 'Napastnik', '1970-1999', '2000-2005', '2006-2010', '2010-2019'
            ],

            players: [],
            tab: null,
            itemsPerPage: 10,

            pagesPlayers: 0,
            currentPagePlayers: 1,
            playersSorted: [],

            pagesTrainers: 0,
            currentPageTrainers: 1,
            trainersSorted: [],

            dialogUpdate: false,
            dialogImage: false,
            dialogDelete: false,
            dialogAdd: false,
            dialogFilter: false,
            
            currentUpdate: {} as Player,
            currentDelete: {} as Player,
            currentAdd: {} as Player,
            currentImage: {} as Player,

            selectedImage: {} as SelectedImage,
            allowedExtensions: ["png", "jpg", "jpeg", "webp"],
            croppedImage: null,
            imageIsCropped: null,

            statuses: [
                { title: 'Nieaktywny', value: 'nieaktywny' },
                { title: 'Aktywny', value: 'aktywny' },
            ],
            positions: [
                { title: 'Bramkarz', value: 'BR' },
                { title: 'Obrońca', value: 'OB' },
                { title: 'Pomocnik', value: 'PO' },
                { title: 'Napastnik', value: 'NA' },
            ],

            searchText: '',

            snackbar: false,
            snackbarError: false,
            snackbarErrorPhoto: false,
            snackbarTimeout: 5000,

            nameRules: [],
            numberRules: [],
            yearRules: [],
            addValid: false,
            updateValid: false,
            deleteValid: false,

            socket: null,
        }
    },
    async created() {
        if (!this.authStore.loggedIn) {
            this.$router.push('/auth/login?action=login');
        }
        if (this.authStore.loggedIn) {
            await this.getAllPlayers();
        }

        this.nameRules = [
            (v) => !!v || this.languageStore.t.rules_email_not,
            (v) => (v && v.length >= 5 && v.length <= 60) || this.languageStore.t.rules_email_length,
        ];
        this.numberRules = [
            (v) => !isNaN(parseFloat(v)) && isFinite(v) && v >= 1 && v <= 99 || 'Number',
        ];

        this.yearRules = [
            (v) => !isNaN(parseFloat(v)) && isFinite(v) && Number.isInteger(parseFloat(v)) && v >= 1970 && v <= 2019 || 'Year',
        ];

        // this.socket = new WebSocket('ws://127.0.0.1:8000/ws/chat/'); // Your WebSocket URL
        // this.socket.onopen = this.onSocketOpen;
        // this.socket.onmessage = this.onSocketMessage;
        // this.socket.onclose = this.onSocketClose;
        // this.socket.onerror = this.onSocketError;
        
    },
    watch: {
        async searchText(newVal) {
            if (newVal === '') {
                await this.getAllPlayers();
                return;
            }
            this.players = await getPlayers(); 
            const filteredPlayers = this.players.filter(player => {
                for (const key in player) {
                    if (key !== 'id') {
                        if (typeof player[key] === 'object') {
                            for (const prop in player[key]) {
                                if (
                                    typeof player[key][prop] === 'string' &&
                                    player[key][prop].toLowerCase().includes(newVal.toLowerCase())
                                ) {
                                    return true;
                                }
                            }
                        } else if (
                            typeof player[key] === 'string' &&
                            player[key].toLowerCase().includes(newVal.toLowerCase())
                        ) {
                            return true;
                        } else if (
                            typeof player[key] === 'number' &&
                            player[key].toString().toLowerCase().includes(newVal.toLowerCase())
                        ) {
                            return true;
                        }
                    }
                }
                return false;
            });
            function filterPlayers(players, filterOptions) {
                return players.filter(player => {
                    const statusCondition =
                    (!filterOptions.statusA || player.status === "aktywny") &&
                    (!filterOptions.statusN || player.status === "nieaktywny");

                    const positionCondition =
                    (!filterOptions.positionB || player.position === "BR") &&
                    (!filterOptions.positionO || player.position === "OB") &&
                    (!filterOptions.positionP || player.position === "PO") &&
                    (!filterOptions.positionN || player.position === "NA");

                    const yearCondition =
                    (!filterOptions.year1 || (parseInt(player.year) >= 1970 && parseInt(player.year) <= 1999)) &&
                    (!filterOptions.year2 || (parseInt(player.year) >= 2000 && parseInt(player.year) <= 2005)) &&
                    (!filterOptions.year3 || (parseInt(player.year) >= 2006 && parseInt(player.year) <= 2010)) &&
                    (!filterOptions.year4 || (parseInt(player.year) >= 2010 && parseInt(player.year) <= 2019));

                    return statusCondition && positionCondition && yearCondition;
                });
            }
            const playersEnd = filterPlayers(filteredPlayers, this.filterOptions)
            this.players = playersEnd;
            this.organizePlayers();
            this.updateSorting();
        }
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
        },
        shouldDisplayFilterDiv() {
            return Object.values(this.filterOptions).some(value => value === true);
        }
    },
    beforeDestroy() {
        if (this.socket) {
            this.socket.close();
        }
    },
    methods: {
        websocketSend() {
            this.socket.send(JSON.stringify({
                'message': 'hello world'
            }))
        },
        onSocketOpen() {
            console.log('WebSocket connected');
        },
        onSocketMessage(event) {
            const data = JSON.parse(event.data);
            console.log('Received data:', data);
        },
        onSocketClose() {
            console.log('WebSocket closed');
        },
        onSocketError(error) {
            console.error('WebSocket error:', error);
        },
        async getAllPlayers() {
            try {
                this.loading = true;
                this.players = await getPlayers(); 
                function filterPlayers(players, filterOptions) {
                    return players.filter(player => {
                        const statusCondition =
                        (!filterOptions.statusA || player.status === "aktywny") &&
                        (!filterOptions.statusN || player.status === "nieaktywny");

                        const positionCondition =
                        (!filterOptions.positionB || player.position === "BR") &&
                        (!filterOptions.positionO || player.position === "OB") &&
                        (!filterOptions.positionP || player.position === "PO") &&
                        (!filterOptions.positionN || player.position === "NA");

                        const yearCondition =
                        (!filterOptions.year1 || (parseInt(player.year) >= 1970 && parseInt(player.year) <= 1999)) &&
                        (!filterOptions.year2 || (parseInt(player.year) >= 2000 && parseInt(player.year) <= 2005)) &&
                        (!filterOptions.year3 || (parseInt(player.year) >= 2006 && parseInt(player.year) <= 2010)) &&
                        (!filterOptions.year4 || (parseInt(player.year) >= 2010 && parseInt(player.year) <= 2019));

                        return statusCondition && positionCondition && yearCondition;
                    });
                }
                this.players = filterPlayers(this.players, this.filterOptions)
                await this.organizePlayers(); 
                this.loading = false;
            } catch (error) {
                console.error(error);
                this.loading = false;
            }
        },
        updatePlayer(id: String, name: String, position: Object, status: Object, number: String, year: String) {
            this.currentUpdate = {
                id: id,
                name: name,
                position: position,
                status: status,
                number: number,
                year: year
            };
            this.dialogUpdate = true;
        },
        updatePlayerClose() {
            this.dialogUpdate = false;
            this.currentUpdate = {};
        },
        imagePlayerClose() {
            this.dialogImage = false;
            this.currentImage = {};
            this.selectedImage = {};
            this.imageIsCropped = null;
        },
        imagePlayer(id: String, name: String, image: String) {
            this.currentImage = {
                id: id,
                name: name,
                image: image,
            }
            this.dialogImage = true;
        },
        async updatePlayerDialog(): Promise<void> {
            this.buttonLoading = true;
            try {
                const valid = await this.$refs.updateValid.validate();
                if (valid) {
                    this.token = await getToken();
                    this.currentUpdate.position = this.currentUpdate.position.value;
                    this.currentUpdate.status = this.currentUpdate.status.value;
                    const response = await updatePlayer(this.token, this.currentUpdate);
                    if (response.status === 0) {
                        await this.getAllPlayers();
                        this.snackbar = true;
                        this.buttonLoading = false;
                        this.dialogUpdate = false;
                        this.currentUpdate = {
                            name: '',
                            position: { title: 'Bramkarz', value: 'BR' },
                            status: { title: 'Aktywny', value: 'aktywny' },
                            number: '',
                            year: ''
                        };
                    } else {
                        this.snackbarError = true;
                        this.buttonLoading = false;
                    }
                } else {
                    this.snackbarError = true;
                    this.buttonLoading = false;
                }
            } catch (error) {
                console.error(error);
                this.snackbarError = true;
                this.buttonLoading = false;
            }
        },
        deletePlayer(id: String, name: String) {
            this.currentDelete = {
                id: id,
                name: name,
            };
            this.dialogDelete = true;
        },
        deletePlayerClose() {
            this.dialogDelete = false;
            this.currentDelete = {};
        },
        async deletePlayerDialog(): Promise<void> {
            this.buttonLoading = true;
            try {
                const valid = await this.$refs.deleteValid.validate();
                if (valid) {
                    this.token = await getToken();
                    const response = await deletePlayer(this.token, this.currentDelete.id);
                    if (response) {
                        await this.getAllPlayers();
                        this.snackbar = true;
                        this.buttonLoading = false;
                        this.dialogDelete = false;
                        this.currentDelete = {
                            name: '',
                            id: ''
                        };
                    } else {
                        this.snackbarError = true;
                        this.buttonLoading = false;
                    }
                } else {
                    this.snackbarError = true;
                    this.buttonLoading = false;
                }
            } catch (error) {
                console.error(error);
                this.snackbarError = true;
                this.buttonLoading = false;
            }
        },
        addPlayer() {
            this.currentAdd = {
                name: '',
                position: {title: 'Bramkarz', value: 'BR'},
                status: {title: 'Aktywny', value: 'aktywny'},
                number: '',
                year: ''
            }
            this.dialogAdd = true;
        },
        addPlayerClose() {
            this.dialogAdd = false; 
            this.currentAdd = {};
        },
        async addPlayerDialog(): Promise<void> {
            this.buttonLoading = true;
            try {
                const valid: boolean = await this.$refs.addValid.validate();
                
                if (valid) {
                    this.token = await getToken();
                    this.currentAdd.position = this.currentAdd.position.value;
                    this.currentAdd.status = this.currentAdd.status.value;
                    
                    const response = await createPlayer(this.token, this.currentAdd);

                    if (response.status === 0) {
                        await this.getAllPlayers();
                        this.snackbar = true;
                        this.buttonLoading = false;
                        this.dialogAdd = false;
                        this.currentAdd = {
                            name: '',
                            position: { title: 'Bramkarz', value: 'BR' },
                            status: { title: 'Aktywny', value: 'aktywny' },
                            number: '',
                            year: ''
                        };
                    } else {
                        this.buttonLoading = false;
                        this.snackbarError = true;
                    }
                } else {
                    this.snackbar = true;
                    this.buttonLoading = false;
                }
            } catch (error) {
                console.error(error);
                this.buttonLoading = false;
                this.snackbarError = true;
            }
        },
        filter() {
            this.dialogFilter = true;
        },
        filterClose() {
            this.dialogFilter = false;
        },
        async updateFilter() {
            this.loading = true;
            this.dialogFilter = false;
            this.players = await getPlayers();

            function filterPlayers(players, filterOptions) {
                return players.filter(player => {
                    const statusCondition =
                    (!filterOptions.statusA || player.status === "aktywny") &&
                    (!filterOptions.statusN || player.status === "nieaktywny");

                    const positionCondition =
                    (!filterOptions.positionB || player.position === "BR") &&
                    (!filterOptions.positionO || player.position === "OB") &&
                    (!filterOptions.positionP || player.position === "PO") &&
                    (!filterOptions.positionN || player.position === "NA");

                    const yearCondition =
                    (!filterOptions.year1 || (parseInt(player.year) >= 1970 && parseInt(player.year) <= 1999)) &&
                    (!filterOptions.year2 || (parseInt(player.year) >= 2000 && parseInt(player.year) <= 2005)) &&
                    (!filterOptions.year3 || (parseInt(player.year) >= 2006 && parseInt(player.year) <= 2010)) &&
                    (!filterOptions.year4 || (parseInt(player.year) >= 2010 && parseInt(player.year) <= 2019));

                    return statusCondition && positionCondition && yearCondition;
                });
            }

            this.players = filterPlayers(this.players, this.filterOptions);
            this.organizePlayers();
            this.loading = false;
        },
        async organizePlayers() {
            let playersToSort = [...this.players];
            for (let i = 0; i < playersToSort.length; i++) {
                if (playersToSort[i].status === 'nieaktywny') {
                    playersToSort[i].status = {title: 'Nieaktywny', value: 'nieaktywny'};
                } else if (playersToSort[i].status === 'aktywny') {
                    playersToSort[i].status = {title: 'Aktywny', value: 'aktywny'};
                }

                if (playersToSort[i].position === 'BR') {
                    playersToSort[i].position = {title: 'Bramkarz', value: 'BR'};
                } else if (playersToSort[i].position === 'OB') {
                    playersToSort[i].position = {title: 'Obrońca', value: 'OB'};
                } else if (playersToSort[i].position === 'PO') {
                    playersToSort[i].position = {title: 'Pomocnik', value: 'PO'};
                } else if (playersToSort[i].position === 'NA') {
                    playersToSort[i].position = {title: 'Napastnik', value: 'NA'};
                }
            }
            this.pagesPlayers = Math.ceil(playersToSort.length / this.itemsPerPage);
            this.playersSorted = [];
            while (playersToSort.length > 0) {
                this.playersSorted.push(playersToSort.splice(0, this.itemsPerPage));
            }
        },
        async changeItemsPerPage(number: Number) {
            this.itemsPerPage = number;
            await this.organizePlayers();
            this.currentPagePlayers = 1;
            this.updateSorting();
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
                    return positionsOrder[a.position.value] - positionsOrder[b.position.value];
                },
                year: (a, b) => a.year - b.year,
                number: (a, b) => a.number - b.number,
                status: (a, b) => {
                    const statusOrder = { aktywny: 0, nieaktywny: 1 };
                    return statusOrder[a.status.value] - statusOrder[b.status.value];
                }
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
            this.organizePlayers();
        },
        previewImage(event) {
            this.loadingImage = true;
            this.imageIsCropped = false;
            const file = event.target.files[0];
            const extension = file.name.split(".").pop().toLowerCase();
            const fileSizeInBytes = file.size;
            const maxSizeInBytes = 1 * 1024 * 1024; // 2MB

            if (!this.allowedExtensions.includes(extension)) {
                this.snackbarErrorPhoto = true;
                return;
            }

            if (fileSizeInBytes > maxSizeInBytes) {
                this.snackbarErrorPhoto = true;
                return;
            }

            const image = new Image();
            image.src = URL.createObjectURL(file);
            image.onload = () => {
                this.selectedImage = {
                    url: image.src,
                    name: file.name,
                };
            };

            this.loadingImage = false;
        },
        isObjectEmpty(obj) {
            return Object.keys(obj).length === 0;
        },
        deleteImagePreview() {
            this.selectedImage = {};
            this.imageIsCropped = null;
        },
        cropImage() {
            const { canvas } = this.$refs.cropper.getResult();
            this.croppedImage = canvas.toDataURL();
            const img = new Image()
            img.onload = () => {
                this.image = img;

                const aspectRatio = img.height / img.width;
                const viewportWidth = window.innerWidth;

                img.width = viewportWidth * 0.9;
                img.height = aspectRatio * viewportWidth;

                if (img.width > 800) {
                    img.width = 800;
                    img.height = aspectRatio * img.width;
                }

                this.$refs.canvas.width = img.width;
                this.$refs.canvas.height = img.height;

                this.ctx = this.$refs.canvas.getContext("2d");
                this.ctx.clearRect(0, 0, this.$refs.canvas.width, this.$refs.canvas.height);
                this.ctx.drawImage(img, 0, 0, img.width, img.height);
            }
            img.src = this.croppedImage;
            this.imageIsCropped = true;
        },
        deleteCanvasImage() {
            const canvas = this.$refs.canvas;
            const ctx = canvas.getContext('2d');
            ctx.clearRect(0, 0, canvas.width, canvas.height);
            this.selectedImage = {};
            this.croppedImage = null;
            this.imageIsCropped = null;
        },
        async imagePlayerDialog() {
            const resultDataURL = this.$refs.canvas.toDataURL('image/webp');
            this.buttonLoading = true;
            this.token = await getToken();

            const formData = new FormData();
            formData.append("playerId", this.currentImage.id);
            formData.append("token", this.token);

            const blob = await fetch(resultDataURL).then(res => res.blob());

            formData.append('image', blob, `${this.currentImage.id}${new Date()}.webp`);

            try {
                const response = await axios.post(`http://127.0.0.1:8000/players/image/`, formData, {
                    headers: {
                        'Content-Type': 'multipart/form-data',
                    },
                });

                if (response.data && response.data.status === 0) {
                    await this.getAllPlayers();
                    this.snackbar = true;
                    this.buttonLoading = false;
                    this.dialogImage = false;
                    this.currentImage = {
                        name: '',
                        id: ''
                    };
                    this.selectedImage = {};
                    this.croppedImage = null;
                    this.imageIsCropped = null;
                } else {
                    this.snackbarError = true;
                    this.buttonLoading = false;
                }
            } catch (error) {
                console.error("Error:", error);
                this.snackbarError = true;
                this.buttonLoading = false;
            }
        },
        changePlayersDirection() {
            this.itemsPerPage = 10;
            const flattened = this.playersSorted.flat();
            
            const reversed = flattened.reverse();

            this.pagesPlayers = Math.ceil(reversed.length / this.itemsPerPage);
            this.currentPagePlayers = 1;
            
            const packed = [];
            for (let i = 0; i < reversed.length; i += 10) {
                packed.push(reversed.slice(i, i + 10));
            }            
            this.playersSorted = packed;
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

input[type="file"] {
    display: none !important;
}
</style>