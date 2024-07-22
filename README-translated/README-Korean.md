# The Turing Way

[![Read the book](https://img.shields.io/badge/read-the%20book-blue.svg)](https://book.the-turing-way.org)
[![Join our tinyletter mailing list](https://img.shields.io/badge/receive-our%20newsletter%20❤%EF%B8%8F-blueviolet.svg)](https://tinyletter.com/TuringWay)
[![Join the chat at https://gitter.im/the-turing-way/the-turing-way](https://img.shields.io/gitter/room/the-turing-way/the-turing-way?logo=gitter)](https://gitter.im/the-turing-way/the-turing-way)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.3233853.svg)](https://doi.org/10.5281/zenodo.3233853)
[![](https://img.shields.io/static/v1?label=TuringWay&message=I%20want%20to%20contribute!&color=yellow&logo=data%3Aimage%2Fpng%3Bbase64%2CiVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8%2F9hAAACYklEQVQ4jXXTy09TQRTH8f5VPhI1xoVxYURNAFcmRleaGDdGXQlKAYkLUARNfICoScGKpTyE3t5bkKD2AUQepUXB0gcgLTalD9rema8LKRVrT3I2k%2Fl95kwyY6BMfQiFqHaoVDlUBoJBZJl9hn8XRsIhqh0abd55tnWdrBA8WfBSpakMhUqhXUCJhKl2aLR65%2FEtLeGc%2BYoy5aHf46bX7cThctK%2BAw2HQkVAW41wzqHRMjNNRteR%2BQzGjg5udZtQ47FiO50gdLZ1nVbvPNUOFSUSxnB4sJ%2F0TjCTTjHk%2BoJl%2BRtqPEaL6zMH79Rw0dyDVVURqRgyn0EkN8jkshwZGsBQodgQyQ2kyDPsce859drjdqLRKE0D%2FZhHR5F6DpHc2B3%2FjF3BcFqxARIpBXXmt9ii67vAYDhIr8fNx0UfE3OzzC0sIHIpxNYqSPEHqFBsiFQMkU3h8vs5%2FvABTeNje6BCj%2FxcwzLlIZHYROq5v4EoIr2JyCbJ57Kobjd3u7o41v4I68pyCfTGrhSvUKHYAJD5bcTWGjKbJJdO4A8E6JyexP4rWgK8Vkb2AjK7hcxnmZybxfF9kff%2BhZJQofvXwhg7O4vAfU2l79ME79xOrjY3c9ZYVzZs8nvZf6%2BRQCRCTgiODg1iCK6vc6WtjZM1tzlRW8sNa99%2Fx64fH%2BNAQz0un49nfh%2BVmspAcKX4lKWUbMbjXOg2cf3Vy%2BLIoRWqekxc7nhB6%2FQ0lZqKJRBAyjKfKZFIcKixgVPPn3LTamFfUyPne7qp1Oz0Bn4g5d7vVAIUamJ2FqPZzCW7gvlHabBQvwE2XnlAiFRrOwAAAABJRU5ErkJggg%3D%3D)](https://github.com/the-turing-way/the-turing-way/blob/main/CONTRIBUTING.md)

_The Turing Way_ 는 재생산 가능한 데이터 사이언스에 대한 가벼운 의견을 제시하는 가이드이다.
이곳에서 읽을 수 있다 : <https://book.the-turing-way.org>
당신은 가이드를 살아있게 만드는 모든 비트들이 있고 가이드를 쓰고 만드는 일이 일어나는 프로젝트 GitHub 저장소를 보고있다.

우리의 목표는 연구원들이 그들의 프로젝트를 시작할 때 필요한 모든 정보를 제공하여 마지막에 쉽게 재현할 수 있도록 하는 것이다.

이것은 또한 박사 과정 학생, 박사후 과정, PI 그리고 자금 지원 팀이 “재현성의 책임” 중 어떤 부분에 영향을 미칠 수 있는지, 그리고 데이터 과학을 보다 효율적이고 효과적이며 이해하기 쉽게 하기 위하여 무엇을 해야 하는지 알도록 하는 것을 의미한다.
내용 목록 : 

- [프로젝트에 대하여](#about-the-project)
- [팀](#the-team)
- [기여](#contributing)
- [The Turing Way 인용](#citing-the-turing-way)
- [연락 취하기](#get-in-touch)
- [기여자](#contributors)

🎧 만약 프로젝트에 대한 음성 소개를 선호한다면, 우리의 팀 구성원 Rachael이 포르투갈의 [Open Science Fair 2019](https://www.opensciencefair.eu/)에서 발표하였으며 그녀의 데모는[Orion podcast](https://orionopenscience.podbean.com/e/the-fair-is-in-town-figshare-the-turing-way-and-open-science-quest-at-the-osfair2019/)에 의하여 녹음되었다.
_The Turing Way_에 대한 개요는 5:13초부터 시작한다.

### 프로젝트에 대한 설명

과학적 연구가 신뢰받을 수 있도록 보장하기 위해서는 재현 가능한 연구가 필요하다.
자금 조달자와 출판사는 출판물에 기초 데이터와 분석 코드에 대한 접근을 포함하도록 요구하기 시작했다.
모든 결과가 향후 작업에서 독립적으로 검증되고 구축될 수 있도록 하는 것이 목표이다.
이것은 때때로 말하기는 쉽지만 행하기는 어렵다.
이러한 연구 결과를 공유한다는 것은 데이터 관리, 도서관학, 소프트웨어 개발 및 지속적인 통합 기술, 즉 학술 연구자와 데이터 과학자에게 널리 가르치거나 기대되지 않는 기술을 이해하는 것을 의미한다.
이러한 활동들은 일반적으로 가르쳐지지 않기 때문에, 우리는 요구 사항과 새로운 기술 습득에 대한 부담이 이 세상에 처음 있는 개인들에게 위협적일 수 있다는 것을 인식한다. 
_The Turing Way_는 이전에 이러한 방식으로 일해 본 적이 없는 사람들에게도 재현 가능한 데이터 과학이 "너무 쉽게 하지 않을" 수 있도록 학생, 감독관, 자금 조달자, 저널 편집자를 지원하기 위한 안내서이다.
여기에는 버전 관리, 분석 테스트, 미래 사용자와의 개방적이고 투명한 커뮤니케이션에 대한 교육 자료가 포함되며 Turing Institute 사례 연구 및 워크샵을 기반으로 한다. 
이 프로젝트는 공개적으로 개발되었으며, 우리의 github 저장소인 <https://github.com/the-turing-way/the-turing-way>에서 모든 질문, 의견 및 추천을 환영한다.

### The team

이것은 튜링 연구소의 프로젝트 팀 기획 업무 중 일부다.
우리에게 더 연락하는 방법을 알고싶으면, [ways of working document](ways_of_working.md)을 봐라.
![Team photo](book/website/figures/TuringWayTeam.jpg)

### 기여

:construction: 이 저장소는 항상 진행중인 작업이며 **모든 사람들**이 다수에게 유용한 무언가를 만드는 것을 도와주기 위하여 격려를 받는다.:construction:

모든 사람들은 우리의 [code of conduct](CODE_OF_CONDUCT.md)를 따라야 하고 시작하기 위한 더 많은 정보를 얻기 위하여 우리의 [contributing guidelines](CONTRIBUTING.md)을 확인해야 한다.

GitHub에 기여하는데 익숙하지 않거나 자신이 없는 경우 [Google submission form](https://goo.gl/forms/akFqZEIy2kxAjfZW2) 제출을 통하여 사례 연구와 팁과 트릭에 기여할 수 있다.

### _The Turing Way_ 인용

DOI: [10.5281/zenodo.3233853](https://doi.org/10.5281/zenodo.3233853)을 사용하여 프로젝트의 Zenodo 아카이브를 통해 _The Turing Way_를 참조할 수 있다.
DOIs 를 사용하면 저장소를 보관할 수 있으며 학술 출판물에서 작업을 추적하는데 매우 유용하다.

인용은 다음과 같다 : 

> The Turing Way Community, Becky Arnold, Louise Bowler, Sarah Gibson, Patricia Herterich, Rosie Higman, … Kirstie Whitaker. (2019, March 25). The Turing Way: A Handbook for Reproducible Data Science (Version v0.0.4). Zenodo. <http://doi.org/10.5281/zenodo.3233986>

당신은 또한 책의 페이지에 사람이 읽을 수 있는 URL을 공유할 수 있다. 예: <https://book.the-turing-way.org/reproducibility/03/definitions.html>, 그러나, 프로젝트는 발전 중이고 이 링크는 바뀔 수 있다는 것을 알아야 한다.
당신은 웹 저장소를 포함하기를 원할 수도 있다. 예: <https://web.archive.org/web/20191030093753/https://book.the-turing-way.org/reproducibility/03/definitions.html> 모든 곳에서 부서진 링크로 끝나지 않는 다는 것을 명심해야 한다.

우리는 _The Truing Way_에 대한 당신의 언급에 진심으로 감사하며 그것이 유용하기를 바란다. 만약 질문이 있다면 [get in touch](#get-in-touch).

### _The Turing Way_ 삽화 인용

_The Turing Way_ 삽화는 2019년 5월 17일 맨체스터, 2019년 5월 28일과 2020년 2월 21일에 런던에서  [_The Turing Way_ book dashes](https://github.com/the-turing-way/the-turing-way/tree/main/workshops/book-dash)의 일부분으로 [Scriberia](https://www.scriberia.co.uk/)의 예술가에 의해 만들어졌다.
그들은 대체적으로 핸드북, 커뮤니티에서 협동하는 노력, _The Turing Way_ 프로젝트를 통해 다양한 내용들을 묘사하였다. 
이런 삽화들은 Zenodo([https://zenodo.org/record/3695300)](https://zenodo.org/record/3695300) 에서 볼 수 있으며 이는 CC-BY license를 사용한다.


만약 이미지를 사용할 것이라면 다음과 같은 내용을 포함해주세요:

>  이 이미지는 Scriberia에서 Turing Way 커뮤니티를 위해 만들어졌으며 CC-BY 라이선스를 사용한다.

제일 최신 버전의 Zenodo는 다음과 같이 인용될 수 있다.:

>  The Turing Way 커뮤니티 & Scriberia (2020년 3월 3일). The Turing Way 책의 삽화. Zenodo. http://doi.org/10.5281/zenodo.3695300

우리는 이 이미지 중의 일부를 사용하였고 이는 이 깃허브 저장소의 새로운 멤버가 기여를 할 때 [Welcome Bot](https://github.com/apps/welcome)가 반응한다.

### 연락 방식

우리는 gitter 채팅방이 있으며  <https://gitter.im/the-turing-way/the-turing-way>에 들리는 것을 매우 반긴다. 
저 채팅방은 [#the-turing-way:matrix.org](https://riot.im/app/#/room/#the-turing-way:matrix.org)의  [Matrix](https://matrix.org)와도 동기화 되어 있으며 당신이 원한다면 우리는 언제나 참여하는 것을 환영한다.
우리는 우리의 프로젝트가 매달 업데이트 되는 사항들을 메일로 보내주는 서비스도 진행한다.
<https://tinyletter.com/TuringWay>을 구독하세요.

당신은 우리 커뮤니티의 매니저 **Malvika Sharan**와 [msharan@turing.ac.uk](mailto:msharan@turing.ac.uk)의 이메일을 통해 연락할 수 있다.
차선책으로는 수석 연구원인 **Kirstie Whitaker**와 [kwhitaker@turing.ac.uk](mailto:kwhitaker@turing.ac.uk)의 이메일을 통해 연락할 수 있다.

## 기여자

이 모든 멋진 사람들에게 감사를 표합니다: ([emoji key](https://allcontributors.org/docs/en/emoji-key)):

[기여자들 목록](https://github.com/the-turing-way/the-turing-way#contributors)

모든 종류의 기여를 환영합니다!
