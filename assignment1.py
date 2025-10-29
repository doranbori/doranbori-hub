def get_file():
    """로그를 작성하려고 시도한 위치를 찾는 함수

    **Logger.log에서 호출되어야만 정상적으로 작동합니다**
    """
    import inspect
    import os

    frame = inspect.stack()[2]
    return os.path.basename(frame.filename)


class Logger:
    """싱글톤 패턴을 적용한 Logger

    실제 실험 코드에서 Logger를 전역 변수로 생성하는 것은 권장되지 않습니다.
    그래서 로그를 남기는 것이 필요한 경우에는 함수 내에서 로거를 가져와야 합니다.
    한 편, 로거를 호출할 때마다 새로운 인스턴스가 생성되면 이것이 불가능하겠죠?

    싱글톤 패턴을 통해 Logger를 여러번 호출하더라도 한 번만 불러와지도록 설계해봅시다!
    `_path`로 지정된 위치에 파일을 만들어서 로그를 차례로 작성하도록 해주세요.

    주의!
    - 기존에 로그 파일이 있었다면, 파일이 덮어씌워지도록 설계되어야 합니다.
    """

    _instance = None
    _path = "test.log"

    def __new__(cls):
        if cls._instance is None:
            cls.single = []
            cls._instance = object.__new__(cls)
        return cls._instance

    def __init__(self): ...

    def log(self, message):
        """로그 작성

        로그는 반드시, [시간 | 호출 위치] > 메세지의 형식으로 작성해주세요.

        e.g. [2025-10-03 21:45:23 | main.py] > Logger가 초기화되었습니다.

        현재 호출 위치는 일반적인 방법으로 찾기 힘들어서, get_file 함수를 만들었습니다. 사용해주세요!

        Args:
            message: 새로운 메세지
        """
        import time

        self.single.append(self._instance)

        if len(self.single) >= 2:
            self._initialized_flag = False  # 이미 초기화 됨

        else:
            self._initialized_flag = True  # 크기가 1이면 새로 초기화 된 것

        if self._initialized_flag:
            now_file_path = get_file()
            origin_time = time.time()
            struct_time = time.localtime(origin_time)
            now = time.strftime("%Y-%m-%d %H:%M:%S", struct_time)
            with open(self._path, "w", encoding="utf-8") as f:
                f.write(f"[{now} | {now_file_path}] > {message}\n")

        elif not self._initialized_flag:
            now_file_path = get_file()
            origin_time = time.time()
            struct_time = time.localtime(origin_time)
            now = time.strftime("%Y-%m-%d %H:%M:%S", struct_time)
            with open(self._path, "a", encoding="utf-8") as f:
                f.write(f"[{now} | {now_file_path}] > {message}\n")

        else:
            raise ValueError("ERROR!")
