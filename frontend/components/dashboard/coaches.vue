<template>
    <section id="table" class="flex flex-col items-center justify-start w-full min-h-[calc(100vh-110px)] text-black bg-[#f5f5f5] h-auto">
        <div v-if="authStore.loggedIn" class="xs:max-w-screen-[450px] sm:max-w-screen-sm md:max-w-screen-md lg:max-w-screen-lg xl:max-w-screen-xl 2xl:max-w-screen-xl w-full h-full flex flex-col justify-center items-center">
            <div class="w-full flex flex-col items-center justify-center">
                <div class="flex flex-row h-[70px] my-2 justify-end w-full items-center">
                    <div class="w-full h-[48px] flex justify-between">
                        <div class="flex">
                            <MainButton :click="filter" type="black" buttonText="Filtruj" class="mr-5" />
                            <div v-if="shouldDisplayFilterDiv" class="flex flex-col font-inter items-start justify-center pr-5">
                                <span class="text-[1rem]">Filtrowanie:</span>
                                <div class="flex flex-row ml-[-6px]">
                                    <span v-for="(key, i) in Object.keys(this.filterOptions)" :key="i" class="text-[0.825rem] text-gray-500 flex flex-row items-start">
                                        <span v-if="this.filterOptions[key] === true" class="flex ml-1 w-full"><v-icon @click="this.filterOptions[key] = false, updateFilter(), this.searchText = ''" class="cursor-pointer">mdi-close</v-icon>{{ this.filterOptionsTranslations[i] }}</span>
                                    </span>
                                </div>
                            </div>
                            <div class="dropdown dropdown-bottom dropdown-end">
                                <MainButton tabindex="0" type="black" buttonText="Sortuj" />
                                <ul class="dropdown-content z-[1] menu p-2 shadow bg-white border-[1px] border-gray-300 rounded-box w-[180px] mt-2">
                                    <li>
                                        <div class="form-control">
                                            <label class="label cursor-pointer">
                                                <input v-model="sortingOptions.type" @change="updateSorting" type="checkbox" class="checkbox checkbox-[#000000] bg-gray-300 border-[1px] border-gray-300 mr-2" />
                                                <span class="label-text">Rola</span> 
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
                            <v-icon @click="changeCoachesDirection()" class="text-white bg-black h-[48px] w-[48px] hover:bg-[#101010] transition ease-in-out duration-300 font-medium rounded-[0.5rem] text-[1rem] ml-5 flex items-center justify-center leading-[1.5] tracking-[0.005em] cursor-pointer">mdi-arrow-up-down</v-icon>
                        </div>
                    </div>
                    <div class="bg-white h-[48px] rounded-[0.5rem] ml-5 min-w-[220px]">
                        <div class="relative h-[48px] flex items-center justify-center">
                            <span class="absolute inset-y-0 left-0 flex items-center pl-3">
                                <v-icon>mdi-magnify</v-icon>
                            </span>
                            <input v-model="searchText" type="stext" class="h-full pl-10 pr-4 py-2 rounded-[0.5rem] block w-full font-inter text-[1rem] leading-[1.5] tracking-[0.005em]" placeholder="Szukaj trenera...">
                            <span v-if="searchText.length > 0" @click="searchText = ''" class="absolute inset-y-0 right-0 flex items-center pr-3 cursor-pointer">
                                <v-icon>mdi-close</v-icon>
                            </span>
                        </div>
                    </div>
                    <MainButton :click="addCoach" type="green" class="bg-green-700 hover:bg-green-800 ml-5" buttonText="Dodaj trenera" :disabled="false" />
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
                                <span class="w-[150px] h-full">Rola</span>
                            </div>
                            <div class="flex items-center justify-center">
                                <span class="w-[120px] h-full">Status</span>
                            </div>
                            <div class="flex items-center justify-center">
                                <span class="w-[150px] h-full">Team</span>
                            </div>
                            <div v-if="this.authStore.user.user.user_type === 'admin'" class="flex items-center justify-center text-center">
                                <span class="w-[120px] h-full">Operacje</span>
                            </div>
                        </div>
                        <div v-if="this.coachesSorted.length === 0" class="w-full h-[599px] border-b-[0.0625rem] border-[hsl(0 0% 92%)] flex items-center justify-center px-10 font-inter text-[#2b2b2b]">
                            <span class="font-inter text-[3rem]">
                                Nic nie znaleziono!
                            </span>
                        </div>
                        <div v-for="(coach, index) in this.coachesSorted[this.currentPageCoaches - 1]" :key="coach.id" :class="{ 'border-b-[0.0625rem] border-[hsl(0 0% 92%)]': index !== this.coachesSorted[this.currentPageCoaches - 1].length - 1 }" class="w-full h-[60px] flex items-center justify-between px-10 font-inter text-[#2b2b2b]">
                            <div class="flex items-center justify-start w-[60px]">
                                <img v-if="coach.image !== null" :src="coach.image" :alt="coach.name" class="w-[50px] h-[50px] rounded-md">
                                <img v-else src="https://st3.depositphotos.com/6672868/13701/v/450/depositphotos_137014128-stock-illustration-user-profile-icon.jpg" alt="placeholder" class="w-[50px] h-[50px] rounded-md">
                            </div>
                            <div class="flex items-center justify-center">
                                <span class="w-[150px] h-full font-[500]">{{coach.name}}</span>
                            </div>
                            <div class="flex items-center justify-center">
                                <span v-if="coach.type.value === 'GW'" class="w-[150px] h-full">Trener główny</span>
                                <span v-if="coach.type.value === 'AS'" class="w-[150px] h-full">Asystent</span>
                            </div>
                            <div class="flex items-center justify-center text-center">
                                <span v-if="coach.status.value === 'nieaktywny'" class="h-full border-[1px] border-red-600 bg-red-50 text-red text-sm rounded-full w-[120px] py-1">Nieaktywny</span>
                                <span v-else class="h-full border-[1px] border-green-600 bg-green-50 text-green text-sm rounded-full w-[120px] py-1">Aktywny</span>
                            </div>
                            <div class="flex items-center justify-center">
                                <span class="w-[150px] h-full">{{coach.team}}</span>
                            </div>
                            <div v-if="this.authStore.user.user.user_type === 'admin'" class="flex items-center justify-center w-[120px]">
                                <v-icon @click="this.updateCoach(coach.id, coach.name, coach.type, coach.status, coach.team)">mdi-pencil-plus</v-icon>
                                <v-icon @click="this.imageCoach(coach.id, coach.name, coach.image)" class="mx-5">mdi-image-edit</v-icon>
                                <v-icon @click="this.deleteCoach(coach.id, coach.name)">mdi-delete</v-icon>
                            </div>
                        </div>
                    </div>
                </article>
                <div v-if="!loading && pagesCoaches > 0" class="w-full h-auto my-5 flex text-black items-center justify-between font-inter">
                    <div class="w-[230px] h-full bg-white rounded-md flex items-center">
                        <select @change="this.changeItemsPerPage(this.itemsPerPage)" v-model="this.itemsPerPage" class="py-3 px-4 block w-[88px] bg-white rounded-[0.5rem] text-sm h-[44px]">
                            <option :value="10">10</option>
                            <option :value="20">20</option>
                            <option :value="50">50</option>
                        </select>
                        <span class="text-sm border-l-[1px] h-full pl-2">Wyniki na stronie</span>
                    </div>
                    <div class="pagination flex items-center justify-center flex-col">
                        <span v-if="this.pagesCoaches > 1" class="flex items-center">
                            <button @click="this.currentPageCoaches = 1" class="text-black w-[35px] h-[35px] cursor-pointer">
                                <v-icon>mdi-chevron-left</v-icon>
                                <v-icon class="ml-[-18px]">mdi-chevron-left</v-icon>
                            </button>
                            <button @click="this.currentPageCoaches--" :disabled="this.currentPageCoaches === 1" class="text-black w-[35px] h-[35px] cursor-pointer">
                                <v-icon>mdi-chevron-left</v-icon>
                            </button>
                            <div v-for="pageNumber in displayedPages" @click="this.currentPageCoaches = pageNumber" :key="pageNumber" class="bg-white w-[35px] h-[35px] mx-1 flex items-center justify-center rounded-md cursor-pointer" :class="{ 'current-page-div': this.currentPageCoaches === pageNumber }">
                                <button :class="{ 'current-page': this.currentPageCoaches === pageNumber }" class="bg-white text-black border-2">
                                    {{ pageNumber }}
                                </button>
                            </div>
                            <button @click="this.currentPageCoaches++" :disabled="this.currentPageCoaches === this.pagesCoaches" class="text-black w-[35px] h-[35px] cursor-pointer">
                                <v-icon>mdi-chevron-right</v-icon>
                            </button>
                            <button @click="this.currentPageCoaches = this.pagesCoaches" class="text-black w-[35px] h-[35px] cursor-pointer">
                                <v-icon>mdi-chevron-right</v-icon>
                                <v-icon class="ml-[-18px]">mdi-chevron-right</v-icon>
                            </button>
                        </span>
                        <span class="mt-2">
                            Strona <b>{{ this.currentPageCoaches }}</b> z <b>{{ this.pagesCoaches }}</b>
                        </span>
                    </div>
                    <div class="w-[230px] h-full flex items-center justify-end">
                        <span class="font-bold">{{ this.coachesSorted[this.currentPageCoaches - 1].length }}</span>
                        <span class="mx-1">z</span>
                        <span class="font-bold">{{ this.coaches.length }}</span>
                    </div>
                </div>
            </div>
            <v-dialog v-model="dialogUpdate" persistent transition="dialog-bottom-transition">
                <v-form @submit.prevent ref="updateValid" v-model="updateValid" class="bg-white h-auto w-[500px] p-10 rounded-[1rem] border-[1px] border-gray-300 shadow-md">
                    <div class="flex flex-row justify-between items-start w-full mb-6">
                        <div class="bg-gray-300 h-[50px] w-[50px] rounded-full flex items-center justify-center">
                            <v-icon>mdi-pencil-plus</v-icon>
                        </div>
                        <v-icon @click="this.dialogUpdate = false; this.currentUpdate = {};" class="cursor-pointer text-gray-500 transition ease-in-out duration-300" style="font-size:28px !important;">mdi-close</v-icon>
                    </div>
                    <div class="flex flex-col mb-7 font-inter">
                        <span class="font-medium mb-5 text-[1.5rem] leading-[1.5] tracking-[0.005em]">Edytowanie trenera.</span>
                        <span class="text-[1rem] text-gray-500 leading-[1.5] tracking-[0.005em] mb-3">Edytujesz dane trenera <b>{{ currentUpdate.name }}</b>.</span>
                        <span class="text-[1rem] text-red-700 leading-[1.5] tracking-[0.005em]">Ta akcja <b>nie może</b> być cofnięta.</span>
                    </div>
                    <div class="flex flex-col mt-3 mb-8 font-inter">
                        <v-text-field v-model="this.currentUpdate.name" :rules="this.nameRules" variant="outlined" class="max-h-[56px] w-full mb-8" placeholder="Name" label="Name"></v-text-field>
                        <v-text-field v-model="this.currentUpdate.team" :rules="this.teamRules" variant="outlined" class="max-h-[56px] w-full mb-8" placeholder="Trenowana drużyna" label="Trenowana drużyna"></v-text-field>
                        <div class="flex flex-row justify-between">
                            <v-select v-model="this.currentUpdate.status" variant="outlined" class="max-h-[56px] max-w-[48%]" :items="statuses" item-title="title" item-value="value" return-object placeholder="Status" label="Status"></v-select>
                            <v-select v-model="this.currentUpdate.type" variant="outlined" class="max-h-[56px] max-w-[48%]" :items="types" item-title="title" item-value="value" return-object placeholder="Position" label="Position"></v-select>
                        </div>
                    </div>
                    <div class="flex flex-row w-full items-center justify-end font-inter">
                        <MainButton :click="updateCoachClose" type="white" buttonText="Anuluj" style="color: black !important;" />
                        <MainButton :click="updateCoachDialog" type="black" :loading="buttonLoading" :disabled="!updateValid" buttonText="Zapisz" class="ml-5" />
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
                    <div class="flex flex-col mb-7 font-inter">
                        <span class="font-medium mb-5 text-[1.5rem] leading-[1.5] tracking-[0.005em]">Edycja zdjęcia zawodnika.</span>
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
                            <MainButton :click="imageCoachClose" type="white" buttonText="Anuluj" style="color: black !important;" />
                            <MainButton :click="deleteImagePreview" type="red" buttonText="Usuń zdjęcie" class="bg-red-700 hover:bg-red-800 ml-5" />
                            <MainButton :click="cropImage" type="green" buttonText="Wytnij" class="bg-green-700 hover:bg-green-800 ml-5" />
                        </div>

                        <canvas v-if="!isObjectEmpty(selectedImage) && this.imageIsCropped" ref="canvas" class="rounded-xl max-h-[600px] w-auto object-contain"></canvas>
                    </div>

                    <div v-if="isObjectEmpty(selectedImage)" class="flex flex-row w-full items-center justify-end font-inter">
                        <MainButton :click="imageCoachClose" type="white" buttonText="Anuluj" style="color: black !important;" />
                        <label v-if="isObjectEmpty(selectedImage)" @click="this.loadingImage = true;" for="file-upload" class="btn h-[40px] text-white bg-blue-700 hover:bg-blue-800 transition ease-in-out duration-300 rounded-[0.5rem] text-[1rem] font-medium px-4 py-1 w-auto flex items-center justify-center font-inter leading-[1.5] tracking-[0.005em] ml-5">
                            Dodaj nowe zdjęcie
                        </label>
                        <input type="file" id="file-upload" ref="fileInput" accept="image/*" @change="previewImage">
                    </div>

                    <div v-if="imageIsCropped && !isObjectEmpty(selectedImage)" class="flex flex-row items-center justify-end mt-10">
                        <MainButton :click="imageCoachClose" type="white" buttonText="Anuluj" style="color: black !important;" />
                        <MainButton v-if="croppedImage !== null" :click="deleteCanvasImage" type="red" buttonText="Usuń zdjęcie" class="bg-red-700 hover:bg-red-800 ml-5" />
                        <Input :icon="false" :click="imageCoachDialog" buttonText="Zapisz zdjęcie" class="ml-5" />
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
                    <div class="flex flex-col mb-7 font-inter">
                        <span class="font-medium mb-5 text-[1.5rem] leading-[1.5] tracking-[0.005em]">Usuwanie zawodnika.</span>
                        <span class="text-[1rem] text-gray-500 leading-[1.5] tracking-[0.005em] mb-3">Czy na pewno chcesz usunąć zawdonika <b>{{ this.currentDelete.name }}</b> z bazy danych?</span>
                        <span class="text-[1rem] text-red-700 leading-[1.5] tracking-[0.005em] mb-3">Ta akcja <b>nie może</b> być cofnięta.</span>
                    </div>
                    <div class="flex flex-row w-full items-center justify-end font-inter">
                        <MainButton :click="deleteCoachClose" type="white" buttonText="Anuluj" style="color: black !important;" />
                        <MainButton :click="deleteCoachDialog" type="red" buttonText="Usuń zawodnika" class="bg-red-700 hover:bg-red-800ml-5" />
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
                    <div class="flex flex-col mb-7 font-inter">
                        <span class="font-medium mb-5 text-[1.5rem] leading-[1.5] tracking-[0.005em]">Dodawanie trenera.</span>
                        <span class="text-[1rem] text-gray-500 leading-[1.5] tracking-[0.005em]">Dodajesz trenera do bazy danych <b>Latarnika Choczewo</b>.</span>
                    </div>
                    <div class="flex flex-col mt-3 mb-8 font-inter">
                        <v-text-field v-model="this.currentAdd.name" :rules="this.nameRules" variant="outlined" class="max-h-[56px] w-full mb-8" placeholder="Name" label="Name"></v-text-field>
                        <v-text-field v-model="this.currentAdd.team" :rules="this.teamRules" variant="outlined" class="max-h-[56px] w-full mb-8" placeholder="Trenowana drużyna" label="Trenowana drużyna"></v-text-field>
                        <div class="flex flex-row justify-between">
                            <v-select v-model="this.currentAdd.status" variant="outlined" class="max-h-[56px] max-w-[48%]" :items="statuses" item-title="title" item-value="value" return-object placeholder="Status" label="Status"></v-select>
                            <v-select v-model="this.currentAdd.type" variant="outlined" class="max-h-[56px] max-w-[48%]" :items="types" item-title="title" item-value="value" return-object placeholder="Rola" label="Rola"></v-select>
                        </div>
                    </div>
                    <div class="flex flex-row w-full items-center justify-end font-inter">
                        <MainButton :click="addCoachClose" type="white" buttonText="Anuluj" style="color: black !important;" />
                        <MainButton :click="addCoachDialog" :loading="buttonLoading" buttonText="Dodaj trenera" :disabled="!addValid" type="green" class="ml-5" />
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
                    <div class="flex flex-col mt-3 mb-8 font-inter">
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
                            <v-icon class="mr-3">mdi-soccer</v-icon>
                            <span class="text-[1rem]">Typ trenera</span>
                        </div>
                        <div class="flex flex-wrap ml-5 mt-2 font-inter text-black">
                            <div class="form-control w-1/2">
                                <label class="label cursor-pointer flex justify-start">
                                    <input v-if="this.filterOptions.typeAS" v-model="filterOptions.typeGW" disabled type="checkbox" class="checkbox checkbox-[#000000] bg-gray-300 border-[1px] border-gray-300 mr-2" />
                                    <input v-else v-model="filterOptions.typeGW" type="checkbox" class="checkbox checkbox-[#000000] bg-gray-300 border-[1px] border-gray-300 mr-2" />
                                    <span class="label-text">Trener główny</span> 
                                </label>
                            </div>
                            <div class="form-control w-1/2">
                                <label class="label cursor-pointer flex justify-start">
                                    <input v-if="this.filterOptions.typeGW" v-model="filterOptions.typeAS" disabled type="checkbox" class="checkbox checkbox-[#000000] bg-gray-300 border-[1px] border-gray-300 mr-2" />
                                    <input v-else v-model="filterOptions.typeAS" type="checkbox" class="checkbox checkbox-[#000000] bg-gray-300 border-[1px] border-gray-300 mr-2" />
                                    <span class="label-text">Asystent</span> 
                                </label>
                            </div>
                        </div>
                    </div>
                    <div class="flex flex-row w-full items-center justify-end font-inter">
                        <MainButton :click="filterClose" type="white" buttonText="Anuluj" style="color: black !important;" />
                        <MainButton :click="updateFilter" type="yellow" buttonText="Filtruj" class="bg-yellow-700 hover:bg-yellow-800 ml-5" style="color: white !important;" />
                    </div>
                </div>
            </v-dialog>
        </div>
        <v-snackbar v-model="snackbar" :timeout="snackbarTimeout" variant="outlined" color="rgba(1, 1, 1, 0)">
            <div class="p-4 my-4 w-[350px] text-sm text-green-600 border-[1px] border-green-900 rounded-lg bg-green-50 text-center flex items-start justify-between" type="alert">
                <span class="font-medium font-inter">{{ this.languageStore.t.auth_sign_up_mess_success }}</span> 
                <v-icon @click="this.snackbar = false;">mdi-close</v-icon>
            </div>
        </v-snackbar>
        <v-snackbar v-model="snackbarError" :timeout="snackbarTimeout" variant="outlined" color="rgba(1, 1, 1, 0)">
            <div class="p-4 my-4 w-[350px] text-sm text-red-600 border-[1px] border-red-900 rounded-lg bg-red-50 text-center" type="alert">
                <span class="font-medium font-inter">{{ this.languageStore.t.auth_login_mess_error }}</span> 
                <v-icon @click="this.snackbarError = false;">mdi-close</v-icon>
            </div>
        </v-snackbar>
        <v-snackbar v-model="snackbarErrorPhoto" :timeout="snackbarTimeout" variant="outlined" color="rgba(1, 1, 1, 0)">
            <div class="p-4 my-4 w-[350px] text-sm text-red-600 border-[1px] border-red-900 rounded-lg bg-red-50 text-center" type="alert">
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
import { getCoaches, updateCoach, createCoach, deleteCoach } from '../../services/coaches/coaches';

import Input from '../elements/Input.vue';
import MainButton from '../elements/MainButton.vue';

import { Cropper } from 'vue-advanced-cropper';
import 'vue-advanced-cropper/dist/style.css'; 

import axios from 'axios';

interface coach {
    age: number;
    type: { value: string };
    year: number;
    number: number;
    image: string;
    status: { value: string };
    name: string;
}

interface SelectedImage {
    name: string;
    url: string;
}

export default{
    components: {
        Cropper,
        MainButton,
        Input,
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
                type: false,
                status: false,
            },

            filterOptions: {
                statusA: false,
                statusN: false,
                typeGW: false,
                typeAS: false,
            },
            filterOptionsTranslations: [
                'Aktywny', 'Nieaktywny', 'Trener główny', 'Asystent',
            ],

            coaches: [],
            tab: null,
            itemsPerPage: 10,

            pagesCoaches: 0,
            currentPageCoaches: 1,
            coachesSorted: [],

            dialogUpdate: false,
            dialogImage: false,
            dialogDelete: false,
            dialogAdd: false,
            dialogFilter: false,
            
            currentUpdate: {} as coach,
            currentDelete: {} as coach,
            currentAdd: {} as coach,
            currentImage: {} as coach,

            selectedImage: {} as SelectedImage,
            allowedExtensions: ["png", "jpg", "jpeg", "webp"],
            croppedImage: null,
            imageIsCropped: null,

            statuses: [
                { title: 'Nieaktywny', value: 'nieaktywny' },
                { title: 'Aktywny', value: 'aktywny' },
            ],
            types: [
                { title: 'Trener Główny', value: 'GW' },
                { title: 'Asystent', value: 'AS' },
            ],

            searchText: '',

            snackbar: false,
            snackbarError: false,
            snackbarErrorPhoto: false,
            snackbarTimeout: 5000,

            nameRules: [],
            teamRules: [],
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
            await this.getAllCoaches();
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
                await this.getAllCoaches();
                return;
            }
            this.coaches = await getCoaches(); 
            const filteredCoaches = this.coaches.filter(coach => {
                for (const key in coach) {
                    if (key !== 'id') {
                        if (typeof coach[key] === 'object') {
                            for (const prop in coach[key]) {
                                if (
                                    typeof coach[key][prop] === 'string' &&
                                    coach[key][prop].toLowerCase().includes(newVal.toLowerCase())
                                ) {
                                    return true;
                                }
                            }
                        } else if (
                            typeof coach[key] === 'string' &&
                            coach[key].toLowerCase().includes(newVal.toLowerCase())
                        ) {
                            return true;
                        } else if (
                            typeof coach[key] === 'number' &&
                            coach[key].toString().toLowerCase().includes(newVal.toLowerCase())
                        ) {
                            return true;
                        }
                    }
                }
                return false;
            });
            function filterCoaches(coaches, filterOptions) {
                return coaches.filter(coach => {
                    const statusCondition =
                    (!filterOptions.statusA || coach.status === "aktywny") &&
                    (!filterOptions.statusN || coach.status === "nieaktywny");

                    const typeCondition =
                    (!filterOptions.typeGW || coach.type === "GW") &&
                    (!filterOptions.typeAS || coach.type === "AS")

                    const yearCondition =
                    (!filterOptions.year1 || (parseInt(coach.year) >= 1970 && parseInt(coach.year) <= 1999)) &&
                    (!filterOptions.year2 || (parseInt(coach.year) >= 2000 && parseInt(coach.year) <= 2005)) &&
                    (!filterOptions.year3 || (parseInt(coach.year) >= 2006 && parseInt(coach.year) <= 2010)) &&
                    (!filterOptions.year4 || (parseInt(coach.year) >= 2010 && parseInt(coach.year) <= 2019));

                    return statusCondition && typeCondition && yearCondition;
                });
            }
            const coachesEnd = filterCoaches(filteredCoaches, this.filterOptions)
            this.coaches = coachesEnd;
            this.organizeCoaches();
            this.updateSorting();
        }
    },
    computed: {
        displayedPages() {
            const maxDisplayed = 5;
            let start;
            let end;

            if (this.pagesCoaches <= maxDisplayed) {
                start = 1;
                end = this.pagesCoaches;
            } else if (this.currentPageCoaches <= Math.floor(maxDisplayed / 2) + 1) {
                start = 1;
                end = maxDisplayed;
            } else if (this.currentPageCoaches >= this.pagesCoaches - Math.floor(maxDisplayed / 2)) {
                start = this.pagesCoaches - maxDisplayed + 1;
                end = this.pagesCoaches;
            } else {
                start = this.currentPageCoaches - Math.floor(maxDisplayed / 2);
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
        async getAllCoaches() {
            try {
                this.loading = true;
                this.coaches = await getCoaches(); 
                function filterCoaches(coaches, filterOptions) {
                    return coaches.filter(coach => {
                        const statusCondition =
                        (!filterOptions.statusA || coach.status === "aktywny") &&
                        (!filterOptions.statusN || coach.status === "nieaktywny");

                        const typeCondition =
                        (!filterOptions.typeGW || coach.type === "GW") &&
                        (!filterOptions.typeAS || coach.type === "AS");

                        const yearCondition =
                        (!filterOptions.year1 || (parseInt(coach.year) >= 1970 && parseInt(coach.year) <= 1999)) &&
                        (!filterOptions.year2 || (parseInt(coach.year) >= 2000 && parseInt(coach.year) <= 2005)) &&
                        (!filterOptions.year3 || (parseInt(coach.year) >= 2006 && parseInt(coach.year) <= 2010)) &&
                        (!filterOptions.year4 || (parseInt(coach.year) >= 2010 && parseInt(coach.year) <= 2019));

                        return statusCondition && typeCondition && yearCondition;
                    });
                }
                this.coaches = filterCoaches(this.coaches, this.filterOptions)
                await this.organizeCoaches(); 
                this.loading = false;
            } catch (error) {
                console.error(error);
                this.loading = false;
            }
        },
        updateCoach(id: String, name: String, type: Object, status: Object, team: String) {
            this.currentUpdate = {
                id: id,
                name: name,
                type: type,
                status: status,
                team: team
            };
            this.dialogUpdate = true;
        },
        updateCoachClose() {
            this.dialogUpdate = false;
            this.currentUpdate = {};
        },
        imageCoachClose() {
            this.dialogImage = false;
            this.currentImage = {};
            this.selectedImage = {};
            this.imageIsCropped = null;
        },
        imageCoach(id: String, name: String, image: String) {
            this.currentImage = {
                id: id,
                name: name,
                image: image,
            }
            this.dialogImage = true;
        },
        async updateCoachDialog(): Promise<void> {
            this.buttonLoading = true;
            try {
                const valid = await this.$refs.updateValid.validate();
                if (valid) {
                    this.token = await getToken();
                    this.currentUpdate.type = this.currentUpdate.type.value;
                    this.currentUpdate.status = this.currentUpdate.status.value;
                    await updateCoach(this.token, this.currentUpdate);
                    await this.getAllCoaches();
                    this.snackbar = true;
                    this.buttonLoading = false;
                    this.dialogUpdate = false;
                    this.currentUpdate = {
                        name: '',
                        type: {title: 'Asystent', value: 'AS'},
                        status: { title: 'Aktywny', value: 'aktywny' },
                        number: '',
                        year: ''
                    };
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
        deleteCoach(id: String, name: String) {
            this.currentDelete = {
                id: id,
                name: name,
            };
            this.dialogDelete = true;
        },
        deleteCoachClose() {
            this.dialogDelete = false;
            this.currentDelete = {};
        },
        async deleteCoachDialog(): Promise<void> {
            this.buttonLoading = true;
            try {
                const valid = await this.$refs.deleteValid.validate();
                if (valid) {
                    this.token = await getToken();
                    const response = await deleteCoach(this.token, this.currentDelete.id);
                    if (response) {
                        await this.getAllCoaches();
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
        addCoach() {
            this.currentAdd = {
                name: '',
                type: {title: 'Asystent', value: 'AS'},
                status: {title: 'Aktywny', value: 'aktywny'},
                team: '',
            }
            this.dialogAdd = true;
        },
        addCoachClose() {
            this.dialogAdd = false; 
            this.currentAdd = {};
        },
        async addCoachDialog(): Promise<void> {
            this.buttonLoading = true;
            try {
                const valid: boolean = await this.$refs.addValid.validate();
                
                if (valid) {
                    this.token = await getToken();
                    this.currentAdd.type = this.currentAdd.type.value;
                    this.currentAdd.status = this.currentAdd.status.value;
                    
                    await createCoach(this.token, this.currentAdd);
                    await this.getAllCoaches();
                    this.snackbar = true;
                    this.buttonLoading = false;
                    this.dialogAdd = false;
                    this.currentAdd = {
                        name: '',
                        type: {title: 'Asystent', value: 'AS'},
                        status: { title: 'Aktywny', value: 'aktywny' },
                        team: '',
                    };
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
        filter(): void {
            this.dialogFilter = true;
        },

        filterClose(): void {
            this.dialogFilter = false;
        },
        async updateFilter(): Promise<void> {
            interface CoachFilter {
                status: string;
                type: string;
                year: string;
            }
    
            interface FilterOptions {
                statusA: boolean;
                statusN: boolean;
                typeGW: boolean;
                typeAS: boolean;
            }
            this.loading = true;
            this.dialogFilter = false;
            this.coaches = await getCoaches();
            this.sortingOptions = {
                type: false,
                status: false,
            };

            const filterCoaches = (coaches: CoachFilter[], filterOptions: FilterOptions): CoachFilter[] => {
                return coaches.filter(coach => {
                    const statusCondition =
                        (!filterOptions.statusA || coach.status === "aktywny") &&
                        (!filterOptions.statusN || coach.status === "nieaktywny");

                    const typeCondition =
                        (!filterOptions.typeGW || coach.type === "GW") &&
                        (!filterOptions.typeAS || coach.type === "AS");
                    const yearCondition =
                        (!filterOptions.year1 || (parseInt(coach.year) >= 1970 && parseInt(coach.year) <= 1999)) &&
                        (!filterOptions.year2 || (parseInt(coach.year) >= 2000 && parseInt(coach.year) <= 2005)) &&
                        (!filterOptions.year3 || (parseInt(coach.year) >= 2006 && parseInt(coach.year) <= 2010)) &&
                        (!filterOptions.year4 || (parseInt(coach.year) >= 2010 && parseInt(coach.year) <= 2019));

                    return statusCondition && typeCondition && yearCondition;
                });
            }

            this.coaches = filterCoaches(this.coaches, this.filterOptions);
            await this.organizeCoaches();
            this.loading = false;
        },
        async organizeCoaches(): Promise<void> {
            interface CoachOrganize {
                status: string | { title: string; value: string };
                type: string | { title: string; value: string };
            }
            let coachesToSort: CoachOrganize[] = [...this.coaches];
            for (let i = 0; i < coachesToSort.length; i++) {
                if (coachesToSort[i].status === 'nieaktywny') {
                    coachesToSort[i].status = {title: 'Nieaktywny', value: 'nieaktywny'};
                } else if (coachesToSort[i].status === 'aktywny') {
                    coachesToSort[i].status = {title: 'Aktywny', value: 'aktywny'};
                }

                if (coachesToSort[i].type === 'GW') {
                    coachesToSort[i].type = {title: 'Trener Główny', value: 'GW'};
                } else if (coachesToSort[i].type === 'AS') {
                    coachesToSort[i].type = {title: 'Asystent', value: 'AS'};
                }
            }
            this.pagesCoaches = Math.ceil(coachesToSort.length / this.itemsPerPage);
            this.coachesSorted = [];
            while (coachesToSort.length > 0) {
                this.coachesSorted.push(coachesToSort.splice(0, this.itemsPerPage));
            }
        },
        async changeItemsPerPage(number: number): Promise<void> {
            this.itemsPerPage = number;
            await this.organizeCoaches();
            this.currentPageCoaches = 1;
            this.updateSorting();
        },
        async getTokenString() {
            return await getToken()
        },
        updateSorting(): void {
            const selectedOptions: string[] = Object.keys(this.sortingOptions).filter(
                (option: string) => this.sortingOptions[option]
            );
            this.sortData(selectedOptions);
        },
        sortData(sortingOptions: string[]): void {
            const sortingFunctions: { [key: string]: (a: coach, b: coach) => number } = {
                type: (a, b) => {
                    const typesOrder = { GW: 0, AS: 1 };
                    return typesOrder[a.type.value] - typesOrder[b.type.value];
                },
                status: (a, b) => {
                    const statusOrder = { aktywny: 0, nieaktywny: 1 };
                    return statusOrder[a.status.value] - statusOrder[b.status.value];
                }
            };

            const sortFunction = (a: coach, b: coach): number => {
                for (const option of sortingOptions) {
                    const result = sortingFunctions[option](a, b);
                    if (result !== 0) {
                        return result;
                    }
                }
                return 0;
            };

            const sortedArray: coach[] = [...this.coaches].sort(sortFunction);
            this.coaches = sortedArray;
            this.organizeCoaches();
        },
        previewImage(event): void {
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
        isObjectEmpty(obj: Record<string, unknown>): boolean {
            return Object.keys(obj).length === 0;
        },
        deleteImagePreview(): void {
            this.selectedImage = {};
            this.imageIsCropped = null;
        },
        cropImage(): void {
            const { canvas } = (this.$refs.cropper as any).getResult();
            this.croppedImage = canvas.toDataURL();
            const img = new Image();
            img.onload = () => {
                this.image = img;

                const aspectRatio: number = img.height / img.width;
                const viewportWidth: number = window.innerWidth;

                img.width = viewportWidth * 0.9;
                img.height = aspectRatio * viewportWidth;

                if (img.width > 800) {
                    img.width = 800;
                    img.height = aspectRatio * img.width;
                }

                (this.$refs.canvas as HTMLCanvasElement).width = img.width;
                (this.$refs.canvas as HTMLCanvasElement).height = img.height;

                this.ctx = (this.$refs.canvas as HTMLCanvasElement).getContext("2d");
                if (this.ctx) {
                    this.ctx.clearRect(0, 0, (this.$refs.canvas as HTMLCanvasElement).width, (this.$refs.canvas as HTMLCanvasElement).height);
                    this.ctx.drawImage(img, 0, 0, img.width, img.height);
                }
            }
            img.src = this.croppedImage;
            this.imageIsCropped = true;
        },
        deleteCanvasImage(): void {
            const canvas = this.$refs.canvas as HTMLCanvasElement;
            const ctx = canvas.getContext('2d');
            if (ctx) {
                ctx.clearRect(0, 0, canvas.width, canvas.height);
            }
            this.selectedImage = {};
            this.croppedImage = null;
            this.imageIsCropped = null;
        },
        async imageCoachDialog(): Promise<void> {
            const resultDataURL: string = (this.$refs.canvas as HTMLCanvasElement).toDataURL('image/webp');
            this.buttonLoading = true;
            this.token = await getToken();

            const formData: FormData = new FormData();
            formData.append("coachId", this.currentImage.id);
            formData.append("token", this.token);

            const response = await fetch(resultDataURL);
            const blob: Blob = await response.blob();

            formData.append('image', blob, `${this.currentImage.id}${new Date()}.webp`);

            try {
                const response = await axios.post(`http://127.0.0.1:8000/players/coach/image/`, formData, {
                    headers: {
                        'Content-Type': 'multipart/form-data',
                    },
                });

                if (response.data && response.data.status === 0) {
                    await this.getAllCoaches();
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
        changeCoachesDirection(): void {
            this.itemsPerPage = 10;
            const flattened: any[] = this.coachesSorted.flat();
            
            const reversed: any[] = flattened.reverse();

            this.pagesCoaches = Math.ceil(reversed.length / this.itemsPerPage);
            this.currentPageCoaches = 1;
            
            const packed: any[][] = [];
            for (let i = 0; i < reversed.length; i += this.itemsPerPage) {
                packed.push(reversed.slice(i, i + this.itemsPerPage));
            }            
            this.coachesSorted = packed;
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