import { ReactNode } from "react";

export default function Home(): ReactNode {
  return (
    <div className="flex justify-center items-center w-full mt-20 mb-10">
      <div className="p-8 rounded-xl bg-white/10 w-11/12 text-center">
        {/** heading */}
        <div>
          <div className="font-bold text-2xl">
            서울시립대 TTS 학술 소모임
          </div>
          <div className="font-bold text-6xl text-shadow-md">
            도란보리
          </div>
        </div>

        <div className="my-4 h-px w-150 bg-[color:var(--chestnut)] justify-self-center"></div>

        <div>
          <div className="text-xl">
            도란보리에 오신 것을 환영합니다!
          </div>

          <button className="mt-10 px-6 py-3 bg-yellow-500 text-black font-semibold rounded-lg hover:bg-yellow-600 transition-colors cursor-pointer">
            <div className="text-black" onClick={() => location.href="/doranbori-hub/docs/intro"}>자습서 바로가기</div>
          </button>
        </div>
      
      </div>
    </div>
  )
}