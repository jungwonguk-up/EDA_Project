{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# 01.Analysis Seoul CCTV"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 1. 데이터 읽기"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "CCTV_Seoul = pd.read_csv('01. Seoul_CCTV.csv', encoding='utf-8')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "read_csv 로 csv 파일을 불러온다.  \n",
    "경로를 정확하게 지정해야함에 유의하자.  \n",
    "encoding = 'utf-8'은 한글이 잘 불러와 지지 않을때 사용한다."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>기관명</th>\n",
       "      <th>소계</th>\n",
       "      <th>2013년도 이전</th>\n",
       "      <th>2014년</th>\n",
       "      <th>2015년</th>\n",
       "      <th>2016년</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>강남구</td>\n",
       "      <td>3238</td>\n",
       "      <td>1292</td>\n",
       "      <td>430</td>\n",
       "      <td>584</td>\n",
       "      <td>932</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>강동구</td>\n",
       "      <td>1010</td>\n",
       "      <td>379</td>\n",
       "      <td>99</td>\n",
       "      <td>155</td>\n",
       "      <td>377</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>강북구</td>\n",
       "      <td>831</td>\n",
       "      <td>369</td>\n",
       "      <td>120</td>\n",
       "      <td>138</td>\n",
       "      <td>204</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>강서구</td>\n",
       "      <td>911</td>\n",
       "      <td>388</td>\n",
       "      <td>258</td>\n",
       "      <td>184</td>\n",
       "      <td>81</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>관악구</td>\n",
       "      <td>2109</td>\n",
       "      <td>846</td>\n",
       "      <td>260</td>\n",
       "      <td>390</td>\n",
       "      <td>613</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   기관명    소계  2013년도 이전  2014년  2015년  2016년\n",
       "0  강남구  3238       1292    430    584    932\n",
       "1  강동구  1010        379     99    155    377\n",
       "2  강북구   831        369    120    138    204\n",
       "3  강서구   911        388    258    184     81\n",
       "4  관악구  2109        846    260    390    613"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "CCTV_Seoul.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "head() 는 엑셀 파일중 상단 5개만 꺼내는 함수이다.  \n",
    "head(3) 이렇게 할 경우 위에서 부터 3개를 꺼낸다."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>기관명</th>\n",
       "      <th>소계</th>\n",
       "      <th>2013년도 이전</th>\n",
       "      <th>2014년</th>\n",
       "      <th>2015년</th>\n",
       "      <th>2016년</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>20</th>\n",
       "      <td>용산구</td>\n",
       "      <td>2096</td>\n",
       "      <td>1368</td>\n",
       "      <td>218</td>\n",
       "      <td>112</td>\n",
       "      <td>398</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>21</th>\n",
       "      <td>은평구</td>\n",
       "      <td>2108</td>\n",
       "      <td>1138</td>\n",
       "      <td>224</td>\n",
       "      <td>278</td>\n",
       "      <td>468</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>22</th>\n",
       "      <td>종로구</td>\n",
       "      <td>1619</td>\n",
       "      <td>464</td>\n",
       "      <td>314</td>\n",
       "      <td>211</td>\n",
       "      <td>630</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>23</th>\n",
       "      <td>중구</td>\n",
       "      <td>1023</td>\n",
       "      <td>413</td>\n",
       "      <td>190</td>\n",
       "      <td>72</td>\n",
       "      <td>348</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>24</th>\n",
       "      <td>중랑구</td>\n",
       "      <td>916</td>\n",
       "      <td>509</td>\n",
       "      <td>121</td>\n",
       "      <td>177</td>\n",
       "      <td>109</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "    기관명    소계  2013년도 이전  2014년  2015년  2016년\n",
       "20  용산구  2096       1368    218    112    398\n",
       "21  은평구  2108       1138    224    278    468\n",
       "22  종로구  1619        464    314    211    630\n",
       "23   중구  1023        413    190     72    348\n",
       "24  중랑구   916        509    121    177    109"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "CCTV_Seoul.tail()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "tail()은 하위 5개를 꺼내는 함수이다.\n",
    "tail(3) 이렇게 할 경우 마찬가지로 하위 3개를 꺼낸다."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Index(['기관명', '소계', '2013년도 이전', '2014년', '2015년', '2016년'], dtype='object')"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "CCTV_Seoul.columns"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    ".colums 는 컬럼을 리스트 형태로 반환하는 함수이다."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'기관명'"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "CCTV_Seoul.columns[0]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [],
   "source": [
    "CCTV_Seoul.rename(\n",
    "    columns={\n",
    "        CCTV_Seoul.columns[0]: '구별'\n",
    "        }, inplace=True\n",
    "    )"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    ".rename = 파일명을 다시 설정  \n",
    "첫번째 컬럼을 기관명에서 구별로 다시 설정해 주었다.  \n",
    "inplace = True 를 해줘야 바뀐게 계속 적용이 된다."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>구별</th>\n",
       "      <th>소계</th>\n",
       "      <th>2013년도 이전</th>\n",
       "      <th>2014년</th>\n",
       "      <th>2015년</th>\n",
       "      <th>2016년</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>강남구</td>\n",
       "      <td>3238</td>\n",
       "      <td>1292</td>\n",
       "      <td>430</td>\n",
       "      <td>584</td>\n",
       "      <td>932</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>강동구</td>\n",
       "      <td>1010</td>\n",
       "      <td>379</td>\n",
       "      <td>99</td>\n",
       "      <td>155</td>\n",
       "      <td>377</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>강북구</td>\n",
       "      <td>831</td>\n",
       "      <td>369</td>\n",
       "      <td>120</td>\n",
       "      <td>138</td>\n",
       "      <td>204</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>강서구</td>\n",
       "      <td>911</td>\n",
       "      <td>388</td>\n",
       "      <td>258</td>\n",
       "      <td>184</td>\n",
       "      <td>81</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>관악구</td>\n",
       "      <td>2109</td>\n",
       "      <td>846</td>\n",
       "      <td>260</td>\n",
       "      <td>390</td>\n",
       "      <td>613</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "    구별    소계  2013년도 이전  2014년  2015년  2016년\n",
       "0  강남구  3238       1292    430    584    932\n",
       "1  강동구  1010        379     99    155    377\n",
       "2  강북구   831        369    120    138    204\n",
       "3  강서구   911        388    258    184     81\n",
       "4  관악구  2109        846    260    390    613"
      ]
     },
     "execution_count": 18,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "CCTV_Seoul.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [],
   "source": [
    "pop_Seoul = pd.read_excel(\n",
    "    '01. Seoul_Population.xls'\n",
    ")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    ".read_excel 함수를 이용해서 엑셀 파일을 불러온다."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>기간</th>\n",
       "      <th>자치구</th>\n",
       "      <th>세대</th>\n",
       "      <th>인구</th>\n",
       "      <th>인구.1</th>\n",
       "      <th>인구.2</th>\n",
       "      <th>인구.3</th>\n",
       "      <th>인구.4</th>\n",
       "      <th>인구.5</th>\n",
       "      <th>인구.6</th>\n",
       "      <th>인구.7</th>\n",
       "      <th>인구.8</th>\n",
       "      <th>세대당인구</th>\n",
       "      <th>65세이상고령자</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>기간</td>\n",
       "      <td>자치구</td>\n",
       "      <td>세대</td>\n",
       "      <td>합계</td>\n",
       "      <td>합계</td>\n",
       "      <td>합계</td>\n",
       "      <td>한국인</td>\n",
       "      <td>한국인</td>\n",
       "      <td>한국인</td>\n",
       "      <td>등록외국인</td>\n",
       "      <td>등록외국인</td>\n",
       "      <td>등록외국인</td>\n",
       "      <td>세대당인구</td>\n",
       "      <td>65세이상고령자</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>기간</td>\n",
       "      <td>자치구</td>\n",
       "      <td>세대</td>\n",
       "      <td>계</td>\n",
       "      <td>남자</td>\n",
       "      <td>여자</td>\n",
       "      <td>계</td>\n",
       "      <td>남자</td>\n",
       "      <td>여자</td>\n",
       "      <td>계</td>\n",
       "      <td>남자</td>\n",
       "      <td>여자</td>\n",
       "      <td>세대당인구</td>\n",
       "      <td>65세이상고령자</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>2017</td>\n",
       "      <td>합계</td>\n",
       "      <td>4220082</td>\n",
       "      <td>10124579</td>\n",
       "      <td>4957857</td>\n",
       "      <td>5166722</td>\n",
       "      <td>9857426</td>\n",
       "      <td>4830206</td>\n",
       "      <td>5027220</td>\n",
       "      <td>267153</td>\n",
       "      <td>127651</td>\n",
       "      <td>139502</td>\n",
       "      <td>2.34</td>\n",
       "      <td>1365126</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>2017</td>\n",
       "      <td>종로구</td>\n",
       "      <td>73594</td>\n",
       "      <td>164257</td>\n",
       "      <td>80094</td>\n",
       "      <td>84163</td>\n",
       "      <td>154770</td>\n",
       "      <td>75967</td>\n",
       "      <td>78803</td>\n",
       "      <td>9487</td>\n",
       "      <td>4127</td>\n",
       "      <td>5360</td>\n",
       "      <td>2.1</td>\n",
       "      <td>26182</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>2017</td>\n",
       "      <td>중구</td>\n",
       "      <td>60412</td>\n",
       "      <td>134593</td>\n",
       "      <td>66337</td>\n",
       "      <td>68256</td>\n",
       "      <td>125709</td>\n",
       "      <td>62253</td>\n",
       "      <td>63456</td>\n",
       "      <td>8884</td>\n",
       "      <td>4084</td>\n",
       "      <td>4800</td>\n",
       "      <td>2.08</td>\n",
       "      <td>21384</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "     기간  자치구       세대        인구     인구.1     인구.2     인구.3     인구.4     인구.5  \\\n",
       "0    기간  자치구       세대        합계       합계       합계      한국인      한국인      한국인   \n",
       "1    기간  자치구       세대         계       남자       여자        계       남자       여자   \n",
       "2  2017   합계  4220082  10124579  4957857  5166722  9857426  4830206  5027220   \n",
       "3  2017  종로구    73594    164257    80094    84163   154770    75967    78803   \n",
       "4  2017   중구    60412    134593    66337    68256   125709    62253    63456   \n",
       "\n",
       "     인구.6    인구.7    인구.8  세대당인구  65세이상고령자  \n",
       "0   등록외국인   등록외국인   등록외국인  세대당인구  65세이상고령자  \n",
       "1       계      남자      여자  세대당인구  65세이상고령자  \n",
       "2  267153  127651  139502   2.34   1365126  \n",
       "3    9487    4127    5360    2.1     26182  \n",
       "4    8884    4084    4800   2.08     21384  "
      ]
     },
     "execution_count": 20,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "pop_Seoul.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [],
   "source": [
    "pop_Seoul = pd.read_excel(\n",
    "    '01. Seoul_Population.xls', header=2, usecols='B,D,G,J,N'\n",
    ")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "header=2 헤더중에서 2번째부터 불러 오겠다.  \n",
    "usecos= 원하는 라인만 쓰겠다."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>자치구</th>\n",
       "      <th>계</th>\n",
       "      <th>계.1</th>\n",
       "      <th>계.2</th>\n",
       "      <th>65세이상고령자</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>합계</td>\n",
       "      <td>10124579</td>\n",
       "      <td>9857426</td>\n",
       "      <td>267153</td>\n",
       "      <td>1365126</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>종로구</td>\n",
       "      <td>164257</td>\n",
       "      <td>154770</td>\n",
       "      <td>9487</td>\n",
       "      <td>26182</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>중구</td>\n",
       "      <td>134593</td>\n",
       "      <td>125709</td>\n",
       "      <td>8884</td>\n",
       "      <td>21384</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>용산구</td>\n",
       "      <td>244444</td>\n",
       "      <td>229161</td>\n",
       "      <td>15283</td>\n",
       "      <td>36882</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>성동구</td>\n",
       "      <td>312711</td>\n",
       "      <td>304808</td>\n",
       "      <td>7903</td>\n",
       "      <td>41273</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   자치구         계      계.1     계.2  65세이상고령자\n",
       "0   합계  10124579  9857426  267153   1365126\n",
       "1  종로구    164257   154770    9487     26182\n",
       "2   중구    134593   125709    8884     21384\n",
       "3  용산구    244444   229161   15283     36882\n",
       "4  성동구    312711   304808    7903     41273"
      ]
     },
     "execution_count": 22,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "pop_Seoul.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>구별</th>\n",
       "      <th>인구수</th>\n",
       "      <th>한국인</th>\n",
       "      <th>외국인</th>\n",
       "      <th>고령자</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>합계</td>\n",
       "      <td>10124579</td>\n",
       "      <td>9857426</td>\n",
       "      <td>267153</td>\n",
       "      <td>1365126</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>종로구</td>\n",
       "      <td>164257</td>\n",
       "      <td>154770</td>\n",
       "      <td>9487</td>\n",
       "      <td>26182</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>중구</td>\n",
       "      <td>134593</td>\n",
       "      <td>125709</td>\n",
       "      <td>8884</td>\n",
       "      <td>21384</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>용산구</td>\n",
       "      <td>244444</td>\n",
       "      <td>229161</td>\n",
       "      <td>15283</td>\n",
       "      <td>36882</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>성동구</td>\n",
       "      <td>312711</td>\n",
       "      <td>304808</td>\n",
       "      <td>7903</td>\n",
       "      <td>41273</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>광진구</td>\n",
       "      <td>372298</td>\n",
       "      <td>357703</td>\n",
       "      <td>14595</td>\n",
       "      <td>43953</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>동대문구</td>\n",
       "      <td>366011</td>\n",
       "      <td>350647</td>\n",
       "      <td>15364</td>\n",
       "      <td>55718</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>중랑구</td>\n",
       "      <td>412780</td>\n",
       "      <td>408226</td>\n",
       "      <td>4554</td>\n",
       "      <td>59262</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>성북구</td>\n",
       "      <td>455407</td>\n",
       "      <td>444055</td>\n",
       "      <td>11352</td>\n",
       "      <td>66251</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9</th>\n",
       "      <td>강북구</td>\n",
       "      <td>328002</td>\n",
       "      <td>324479</td>\n",
       "      <td>3523</td>\n",
       "      <td>56530</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>10</th>\n",
       "      <td>도봉구</td>\n",
       "      <td>346234</td>\n",
       "      <td>344166</td>\n",
       "      <td>2068</td>\n",
       "      <td>53488</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>11</th>\n",
       "      <td>노원구</td>\n",
       "      <td>558075</td>\n",
       "      <td>554403</td>\n",
       "      <td>3672</td>\n",
       "      <td>74243</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>12</th>\n",
       "      <td>은평구</td>\n",
       "      <td>491202</td>\n",
       "      <td>486794</td>\n",
       "      <td>4408</td>\n",
       "      <td>74559</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>13</th>\n",
       "      <td>서대문구</td>\n",
       "      <td>325028</td>\n",
       "      <td>312800</td>\n",
       "      <td>12228</td>\n",
       "      <td>49266</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>14</th>\n",
       "      <td>마포구</td>\n",
       "      <td>385783</td>\n",
       "      <td>374915</td>\n",
       "      <td>10868</td>\n",
       "      <td>49615</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>15</th>\n",
       "      <td>양천구</td>\n",
       "      <td>475018</td>\n",
       "      <td>471154</td>\n",
       "      <td>3864</td>\n",
       "      <td>55234</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>16</th>\n",
       "      <td>강서구</td>\n",
       "      <td>608255</td>\n",
       "      <td>601691</td>\n",
       "      <td>6564</td>\n",
       "      <td>76032</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>17</th>\n",
       "      <td>구로구</td>\n",
       "      <td>441559</td>\n",
       "      <td>410742</td>\n",
       "      <td>30817</td>\n",
       "      <td>58794</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>18</th>\n",
       "      <td>금천구</td>\n",
       "      <td>253491</td>\n",
       "      <td>235154</td>\n",
       "      <td>18337</td>\n",
       "      <td>34170</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>19</th>\n",
       "      <td>영등포구</td>\n",
       "      <td>402024</td>\n",
       "      <td>368550</td>\n",
       "      <td>33474</td>\n",
       "      <td>53981</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>20</th>\n",
       "      <td>동작구</td>\n",
       "      <td>408493</td>\n",
       "      <td>396217</td>\n",
       "      <td>12276</td>\n",
       "      <td>57255</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>21</th>\n",
       "      <td>관악구</td>\n",
       "      <td>520929</td>\n",
       "      <td>503297</td>\n",
       "      <td>17632</td>\n",
       "      <td>70046</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>22</th>\n",
       "      <td>서초구</td>\n",
       "      <td>445401</td>\n",
       "      <td>441102</td>\n",
       "      <td>4299</td>\n",
       "      <td>53205</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>23</th>\n",
       "      <td>강남구</td>\n",
       "      <td>561052</td>\n",
       "      <td>556164</td>\n",
       "      <td>4888</td>\n",
       "      <td>65060</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>24</th>\n",
       "      <td>송파구</td>\n",
       "      <td>671173</td>\n",
       "      <td>664496</td>\n",
       "      <td>6677</td>\n",
       "      <td>76582</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25</th>\n",
       "      <td>강동구</td>\n",
       "      <td>440359</td>\n",
       "      <td>436223</td>\n",
       "      <td>4136</td>\n",
       "      <td>56161</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "      구별       인구수      한국인     외국인      고령자\n",
       "0     합계  10124579  9857426  267153  1365126\n",
       "1    종로구    164257   154770    9487    26182\n",
       "2     중구    134593   125709    8884    21384\n",
       "3    용산구    244444   229161   15283    36882\n",
       "4    성동구    312711   304808    7903    41273\n",
       "5    광진구    372298   357703   14595    43953\n",
       "6   동대문구    366011   350647   15364    55718\n",
       "7    중랑구    412780   408226    4554    59262\n",
       "8    성북구    455407   444055   11352    66251\n",
       "9    강북구    328002   324479    3523    56530\n",
       "10   도봉구    346234   344166    2068    53488\n",
       "11   노원구    558075   554403    3672    74243\n",
       "12   은평구    491202   486794    4408    74559\n",
       "13  서대문구    325028   312800   12228    49266\n",
       "14   마포구    385783   374915   10868    49615\n",
       "15   양천구    475018   471154    3864    55234\n",
       "16   강서구    608255   601691    6564    76032\n",
       "17   구로구    441559   410742   30817    58794\n",
       "18   금천구    253491   235154   18337    34170\n",
       "19  영등포구    402024   368550   33474    53981\n",
       "20   동작구    408493   396217   12276    57255\n",
       "21   관악구    520929   503297   17632    70046\n",
       "22   서초구    445401   441102    4299    53205\n",
       "23   강남구    561052   556164    4888    65060\n",
       "24   송파구    671173   664496    6677    76582\n",
       "25   강동구    440359   436223    4136    56161"
      ]
     },
     "execution_count": 23,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "pop_Seoul.rename(\n",
    "    columns={\n",
    "        pop_Seoul.columns[0]: '구별',\n",
    "        pop_Seoul.columns[1]: '인구수',\n",
    "        pop_Seoul.columns[2]: '한국인',\n",
    "        pop_Seoul.columns[3]: '외국인',\n",
    "        pop_Seoul.columns[4]: '고령자',\n",
    "    }\n",
    ")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## pandas 기초\n",
    "- Python에서 R 만큼의 강력한 데이터 핸들링 성능을 제공하는 모듈\n",
    "- 단일 프로세스에서는 최대 효율\n",
    "- 코딩 가능하고 으용 가능한 엑셀로 받아들여도 됨\n",
    "- 누군가 스테로이드를 맞은 엑셀로 표현함"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Series\n",
    "- dex와 value로 이루어져 있습니다.  \n",
    "- 한 가지 데이터 타입만 가질 수 있습니다."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import numpy as np"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "- pandas는 통상 pd\n",
    "- numpy는 통상 np"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\jcc96\\AppData\\Local\\Temp/ipykernel_4552/2031691219.py:1: FutureWarning: The default dtype for empty Series will be 'object' instead of 'float64' in a future version. Specify a dtype explicitly to silence this warning.\n",
      "  pd.Series()\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "Series([], dtype: float64)"
      ]
     },
     "execution_count": 25,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "pd.Series()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "위와 같이 어떻게 작성해야할지 모를땐 그냥 쳐보면 밑에 오류에서 파악할 수 있다.  \n",
    "리스트 형태이고, 플롯 값이 들어감을 알 수있다."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0    1\n",
       "1    2\n",
       "2    3\n",
       "3    4\n",
       "dtype: int64"
      ]
     },
     "execution_count": 26,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "pd.Series([1, 2, 3, 4])"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "int형을 플롯형으로 바꿔줘야 할것 같으므로 진행해본다"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'float64' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m~\\AppData\\Local\\Temp/ipykernel_4552/1502664684.py\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[0mpd\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mSeries\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;36m1\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;36m2\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;36m3\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;36m4\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mdtype\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mfloat64\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m: name 'float64' is not defined"
     ]
    }
   ],
   "source": [
    "pd.Series([1, 2, 3, 4], dtype=float64)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "float64가 정의되있지 않다고 한다.  \n",
    "해결법을 모르니 구글에 pandas.Series 를 검색하여 가이드를 확인한다"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0    1.0\n",
       "1    2.0\n",
       "2    3.0\n",
       "3    4.0\n",
       "dtype: float64"
      ]
     },
     "execution_count": 28,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "pd.Series([1, 2, 3, 4], dtype=np.float64)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0    1\n",
       "1    2\n",
       "2    3\n",
       "3    4\n",
       "dtype: object"
      ]
     },
     "execution_count": 29,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "pd.Series([1, 2, 3, 4], dtype=str)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "주피터 pandas에서 object는 파이썬에서 str과 같은 의미이다"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0    1\n",
       "1    2\n",
       "2    3\n",
       "dtype: int32"
      ]
     },
     "execution_count": 30,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "pd.Series(np.array([1, 2, 3]))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Key    Value\n",
       "dtype: object"
      ]
     },
     "execution_count": 31,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "pd.Series({'Key': 'Value'})"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0    1\n",
       "1    2\n",
       "2    3\n",
       "3    4\n",
       "4    5\n",
       "dtype: object"
      ]
     },
     "execution_count": 33,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data = pd.Series([1, 2, 3, 4, '5'])\n",
    "data"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "대부분이 int지만 출력물은 object 이다."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "metadata": {},
   "outputs": [
    {
     "ename": "TypeError",
     "evalue": "not all arguments converted during string formatting",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m~\\anaconda3\\envs\\ds_study\\lib\\site-packages\\pandas\\core\\ops\\array_ops.py\u001b[0m in \u001b[0;36m_na_arithmetic_op\u001b[1;34m(left, right, op, is_cmp)\u001b[0m\n\u001b[0;32m    162\u001b[0m     \u001b[1;32mtry\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 163\u001b[1;33m         \u001b[0mresult\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mfunc\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mleft\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mright\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    164\u001b[0m     \u001b[1;32mexcept\u001b[0m \u001b[0mTypeError\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\anaconda3\\envs\\ds_study\\lib\\site-packages\\pandas\\core\\computation\\expressions.py\u001b[0m in \u001b[0;36mevaluate\u001b[1;34m(op, a, b, use_numexpr)\u001b[0m\n\u001b[0;32m    239\u001b[0m             \u001b[1;32mreturn\u001b[0m \u001b[0m_evaluate\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mop\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mop_str\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0ma\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mb\u001b[0m\u001b[1;33m)\u001b[0m  \u001b[1;31m# type: ignore[misc]\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 240\u001b[1;33m     \u001b[1;32mreturn\u001b[0m \u001b[0m_evaluate_standard\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mop\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mop_str\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0ma\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mb\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    241\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\anaconda3\\envs\\ds_study\\lib\\site-packages\\pandas\\core\\computation\\expressions.py\u001b[0m in \u001b[0;36m_evaluate_standard\u001b[1;34m(op, op_str, a, b)\u001b[0m\n\u001b[0;32m     68\u001b[0m         \u001b[0m_store_test_result\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;32mFalse\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m---> 69\u001b[1;33m     \u001b[1;32mreturn\u001b[0m \u001b[0mop\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0ma\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mb\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m     70\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mTypeError\u001b[0m: not all arguments converted during string formatting",
      "\nDuring handling of the above exception, another exception occurred:\n",
      "\u001b[1;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m~\\AppData\\Local\\Temp/ipykernel_4552/831588745.py\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      1\u001b[0m \u001b[1;31m#짝수를 찾고 싶다.\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 2\u001b[1;33m \u001b[0mdata\u001b[0m\u001b[1;33m%\u001b[0m\u001b[1;36m2\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;32m~\\anaconda3\\envs\\ds_study\\lib\\site-packages\\pandas\\core\\ops\\common.py\u001b[0m in \u001b[0;36mnew_method\u001b[1;34m(self, other)\u001b[0m\n\u001b[0;32m     68\u001b[0m         \u001b[0mother\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mitem_from_zerodim\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mother\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     69\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m---> 70\u001b[1;33m         \u001b[1;32mreturn\u001b[0m \u001b[0mmethod\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mother\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m     71\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     72\u001b[0m     \u001b[1;32mreturn\u001b[0m \u001b[0mnew_method\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\anaconda3\\envs\\ds_study\\lib\\site-packages\\pandas\\core\\arraylike.py\u001b[0m in \u001b[0;36m__mod__\u001b[1;34m(self, other)\u001b[0m\n\u001b[0;32m    138\u001b[0m     \u001b[1;33m@\u001b[0m\u001b[0munpack_zerodim_and_defer\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m\"__mod__\"\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    139\u001b[0m     \u001b[1;32mdef\u001b[0m \u001b[0m__mod__\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mother\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 140\u001b[1;33m         \u001b[1;32mreturn\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_arith_method\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mother\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0moperator\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mmod\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    141\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    142\u001b[0m     \u001b[1;33m@\u001b[0m\u001b[0munpack_zerodim_and_defer\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m\"__rmod__\"\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\anaconda3\\envs\\ds_study\\lib\\site-packages\\pandas\\core\\series.py\u001b[0m in \u001b[0;36m_arith_method\u001b[1;34m(self, other, op)\u001b[0m\n\u001b[0;32m   5637\u001b[0m     \u001b[1;32mdef\u001b[0m \u001b[0m_arith_method\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mother\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mop\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m   5638\u001b[0m         \u001b[0mself\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mother\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mops\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0malign_method_SERIES\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mother\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m-> 5639\u001b[1;33m         \u001b[1;32mreturn\u001b[0m \u001b[0mbase\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mIndexOpsMixin\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_arith_method\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mother\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mop\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m   5640\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m   5641\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\anaconda3\\envs\\ds_study\\lib\\site-packages\\pandas\\core\\base.py\u001b[0m in \u001b[0;36m_arith_method\u001b[1;34m(self, other, op)\u001b[0m\n\u001b[0;32m   1293\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m   1294\u001b[0m         \u001b[1;32mwith\u001b[0m \u001b[0mnp\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0merrstate\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mall\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;34m\"ignore\"\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m-> 1295\u001b[1;33m             \u001b[0mresult\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mops\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0marithmetic_op\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mlvalues\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mrvalues\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mop\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m   1296\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m   1297\u001b[0m         \u001b[1;32mreturn\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_construct_result\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mresult\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mname\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mres_name\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\anaconda3\\envs\\ds_study\\lib\\site-packages\\pandas\\core\\ops\\array_ops.py\u001b[0m in \u001b[0;36marithmetic_op\u001b[1;34m(left, right, op)\u001b[0m\n\u001b[0;32m    220\u001b[0m         \u001b[0m_bool_arith_check\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mop\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mleft\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mright\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    221\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 222\u001b[1;33m         \u001b[0mres_values\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0m_na_arithmetic_op\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mleft\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mright\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mop\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    223\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    224\u001b[0m     \u001b[1;32mreturn\u001b[0m \u001b[0mres_values\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\anaconda3\\envs\\ds_study\\lib\\site-packages\\pandas\\core\\ops\\array_ops.py\u001b[0m in \u001b[0;36m_na_arithmetic_op\u001b[1;34m(left, right, op, is_cmp)\u001b[0m\n\u001b[0;32m    168\u001b[0m             \u001b[1;31m# Don't do this for comparisons, as that will handle complex numbers\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    169\u001b[0m             \u001b[1;31m#  incorrectly, see GH#32047\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 170\u001b[1;33m             \u001b[0mresult\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0m_masked_arith_op\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mleft\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mright\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mop\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    171\u001b[0m         \u001b[1;32melse\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    172\u001b[0m             \u001b[1;32mraise\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\anaconda3\\envs\\ds_study\\lib\\site-packages\\pandas\\core\\ops\\array_ops.py\u001b[0m in \u001b[0;36m_masked_arith_op\u001b[1;34m(x, y, op)\u001b[0m\n\u001b[0;32m    125\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    126\u001b[0m         \u001b[1;32mif\u001b[0m \u001b[0mmask\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0many\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 127\u001b[1;33m             \u001b[0mresult\u001b[0m\u001b[1;33m[\u001b[0m\u001b[0mmask\u001b[0m\u001b[1;33m]\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mop\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mxrav\u001b[0m\u001b[1;33m[\u001b[0m\u001b[0mmask\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0my\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    128\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    129\u001b[0m     \u001b[0mnp\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mputmask\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mresult\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;33m~\u001b[0m\u001b[0mmask\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mnp\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mnan\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mTypeError\u001b[0m: not all arguments converted during string formatting"
     ]
    }
   ],
   "source": [
    "#짝수를 찾고 싶다.\n",
    "data%2"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "not all arguments converted during string formatting 를 읽어보면 str이 문제가 됨을 알 수 있다."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 날짜 데이터"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "DatetimeIndex(['2021-01-01', '2021-01-02', '2021-01-03', '2021-01-04',\n",
       "               '2021-01-05', '2021-01-06'],\n",
       "              dtype='datetime64[ns]', freq='D')"
      ]
     },
     "execution_count": 42,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "dates = pd.date_range('20210101', periods=6)\n",
    "dates"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### DataFrame\n",
    "- pd.Series()\n",
    "    - index, value\n",
    "- pd.DataFrame()\n",
    "    - index, value, column"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[ 0.54961592,  1.42094603, -1.05839241,  0.9109797 ],\n",
       "       [ 1.22761118,  0.79608411,  0.59279598, -0.20091472],\n",
       "       [-0.08129009,  0.85022078, -0.41851623, -0.20551821],\n",
       "       [ 0.14996783,  0.53368343,  0.16853839, -0.99076167],\n",
       "       [ 2.52669411,  0.89396024, -0.10031101,  0.00913617],\n",
       "       [ 0.10605774, -0.13516601,  0.37750192, -0.85430128]])"
      ]
     },
     "execution_count": 36,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# 표준정규분포에서 샘플링한 난수 생성\n",
    "data = np.random.randn(6,4)\n",
    "data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>A</th>\n",
       "      <th>B</th>\n",
       "      <th>C</th>\n",
       "      <th>D</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>2021-01-01</th>\n",
       "      <td>0.549616</td>\n",
       "      <td>1.420946</td>\n",
       "      <td>-1.058392</td>\n",
       "      <td>0.910980</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2021-01-02</th>\n",
       "      <td>1.227611</td>\n",
       "      <td>0.796084</td>\n",
       "      <td>0.592796</td>\n",
       "      <td>-0.200915</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2021-01-03</th>\n",
       "      <td>-0.081290</td>\n",
       "      <td>0.850221</td>\n",
       "      <td>-0.418516</td>\n",
       "      <td>-0.205518</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2021-01-04</th>\n",
       "      <td>0.149968</td>\n",
       "      <td>0.533683</td>\n",
       "      <td>0.168538</td>\n",
       "      <td>-0.990762</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2021-01-05</th>\n",
       "      <td>2.526694</td>\n",
       "      <td>0.893960</td>\n",
       "      <td>-0.100311</td>\n",
       "      <td>0.009136</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2021-01-06</th>\n",
       "      <td>0.106058</td>\n",
       "      <td>-0.135166</td>\n",
       "      <td>0.377502</td>\n",
       "      <td>-0.854301</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                   A         B         C         D\n",
       "2021-01-01  0.549616  1.420946 -1.058392  0.910980\n",
       "2021-01-02  1.227611  0.796084  0.592796 -0.200915\n",
       "2021-01-03 -0.081290  0.850221 -0.418516 -0.205518\n",
       "2021-01-04  0.149968  0.533683  0.168538 -0.990762\n",
       "2021-01-05  2.526694  0.893960 -0.100311  0.009136\n",
       "2021-01-06  0.106058 -0.135166  0.377502 -0.854301"
      ]
     },
     "execution_count": 45,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df = pd.DataFrame(data, index=dates, columns=['A', 'B', 'C', 'D'])\n",
    "df"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 데이터 프레임 정보 탐색"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "- df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>A</th>\n",
       "      <th>B</th>\n",
       "      <th>C</th>\n",
       "      <th>D</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>2021-01-01</th>\n",
       "      <td>0.549616</td>\n",
       "      <td>1.420946</td>\n",
       "      <td>-1.058392</td>\n",
       "      <td>0.910980</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2021-01-02</th>\n",
       "      <td>1.227611</td>\n",
       "      <td>0.796084</td>\n",
       "      <td>0.592796</td>\n",
       "      <td>-0.200915</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2021-01-03</th>\n",
       "      <td>-0.081290</td>\n",
       "      <td>0.850221</td>\n",
       "      <td>-0.418516</td>\n",
       "      <td>-0.205518</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2021-01-04</th>\n",
       "      <td>0.149968</td>\n",
       "      <td>0.533683</td>\n",
       "      <td>0.168538</td>\n",
       "      <td>-0.990762</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2021-01-05</th>\n",
       "      <td>2.526694</td>\n",
       "      <td>0.893960</td>\n",
       "      <td>-0.100311</td>\n",
       "      <td>0.009136</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                   A         B         C         D\n",
       "2021-01-01  0.549616  1.420946 -1.058392  0.910980\n",
       "2021-01-02  1.227611  0.796084  0.592796 -0.200915\n",
       "2021-01-03 -0.081290  0.850221 -0.418516 -0.205518\n",
       "2021-01-04  0.149968  0.533683  0.168538 -0.990762\n",
       "2021-01-05  2.526694  0.893960 -0.100311  0.009136"
      ]
     },
     "execution_count": 46,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "- df.tail"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>A</th>\n",
       "      <th>B</th>\n",
       "      <th>C</th>\n",
       "      <th>D</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>2021-01-02</th>\n",
       "      <td>1.227611</td>\n",
       "      <td>0.796084</td>\n",
       "      <td>0.592796</td>\n",
       "      <td>-0.200915</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2021-01-03</th>\n",
       "      <td>-0.081290</td>\n",
       "      <td>0.850221</td>\n",
       "      <td>-0.418516</td>\n",
       "      <td>-0.205518</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2021-01-04</th>\n",
       "      <td>0.149968</td>\n",
       "      <td>0.533683</td>\n",
       "      <td>0.168538</td>\n",
       "      <td>-0.990762</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2021-01-05</th>\n",
       "      <td>2.526694</td>\n",
       "      <td>0.893960</td>\n",
       "      <td>-0.100311</td>\n",
       "      <td>0.009136</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2021-01-06</th>\n",
       "      <td>0.106058</td>\n",
       "      <td>-0.135166</td>\n",
       "      <td>0.377502</td>\n",
       "      <td>-0.854301</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                   A         B         C         D\n",
       "2021-01-02  1.227611  0.796084  0.592796 -0.200915\n",
       "2021-01-03 -0.081290  0.850221 -0.418516 -0.205518\n",
       "2021-01-04  0.149968  0.533683  0.168538 -0.990762\n",
       "2021-01-05  2.526694  0.893960 -0.100311  0.009136\n",
       "2021-01-06  0.106058 -0.135166  0.377502 -0.854301"
      ]
     },
     "execution_count": 47,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.tail()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "- df.index"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "DatetimeIndex(['2021-01-01', '2021-01-02', '2021-01-03', '2021-01-04',\n",
       "               '2021-01-05', '2021-01-06'],\n",
       "              dtype='datetime64[ns]', freq='D')"
      ]
     },
     "execution_count": 49,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.index"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Index(['A', 'B', 'C', 'D'], dtype='object')"
      ]
     },
     "execution_count": 50,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.columns"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 51,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[ 0.54961592,  1.42094603, -1.05839241,  0.9109797 ],\n",
       "       [ 1.22761118,  0.79608411,  0.59279598, -0.20091472],\n",
       "       [-0.08129009,  0.85022078, -0.41851623, -0.20551821],\n",
       "       [ 0.14996783,  0.53368343,  0.16853839, -0.99076167],\n",
       "       [ 2.52669411,  0.89396024, -0.10031101,  0.00913617],\n",
       "       [ 0.10605774, -0.13516601,  0.37750192, -0.85430128]])"
      ]
     },
     "execution_count": 51,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.values"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "head() / tail() 은 괄호가 붙는데 매소드이 이기 때문이고,  \n",
    "index / columns / values 는 변수이기 때문에 그냥 쓰는것이다."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "- df.info() : 데이터 프레임의 기본 정보 확인"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 52,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "DatetimeIndex: 6 entries, 2021-01-01 to 2021-01-06\n",
      "Freq: D\n",
      "Data columns (total 4 columns):\n",
      " #   Column  Non-Null Count  Dtype  \n",
      "---  ------  --------------  -----  \n",
      " 0   A       6 non-null      float64\n",
      " 1   B       6 non-null      float64\n",
      " 2   C       6 non-null      float64\n",
      " 3   D       6 non-null      float64\n",
      "dtypes: float64(4)\n",
      "memory usage: 240.0 bytes\n"
     ]
    }
   ],
   "source": [
    "df.info()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "- df.describe() : 데이터 프레임의 기술통계 정보 확인"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 53,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>A</th>\n",
       "      <th>B</th>\n",
       "      <th>C</th>\n",
       "      <th>D</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>count</th>\n",
       "      <td>6.000000</td>\n",
       "      <td>6.000000</td>\n",
       "      <td>6.000000</td>\n",
       "      <td>6.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>mean</th>\n",
       "      <td>0.746443</td>\n",
       "      <td>0.726621</td>\n",
       "      <td>-0.073064</td>\n",
       "      <td>-0.221897</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>std</th>\n",
       "      <td>0.988997</td>\n",
       "      <td>0.511878</td>\n",
       "      <td>0.599283</td>\n",
       "      <td>0.682434</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>min</th>\n",
       "      <td>-0.081290</td>\n",
       "      <td>-0.135166</td>\n",
       "      <td>-1.058392</td>\n",
       "      <td>-0.990762</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25%</th>\n",
       "      <td>0.117035</td>\n",
       "      <td>0.599284</td>\n",
       "      <td>-0.338965</td>\n",
       "      <td>-0.692106</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>50%</th>\n",
       "      <td>0.349792</td>\n",
       "      <td>0.823152</td>\n",
       "      <td>0.034114</td>\n",
       "      <td>-0.203216</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>75%</th>\n",
       "      <td>1.058112</td>\n",
       "      <td>0.883025</td>\n",
       "      <td>0.325261</td>\n",
       "      <td>-0.043377</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>max</th>\n",
       "      <td>2.526694</td>\n",
       "      <td>1.420946</td>\n",
       "      <td>0.592796</td>\n",
       "      <td>0.910980</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "              A         B         C         D\n",
       "count  6.000000  6.000000  6.000000  6.000000\n",
       "mean   0.746443  0.726621 -0.073064 -0.221897\n",
       "std    0.988997  0.511878  0.599283  0.682434\n",
       "min   -0.081290 -0.135166 -1.058392 -0.990762\n",
       "25%    0.117035  0.599284 -0.338965 -0.692106\n",
       "50%    0.349792  0.823152  0.034114 -0.203216\n",
       "75%    1.058112  0.883025  0.325261 -0.043377\n",
       "max    2.526694  1.420946  0.592796  0.910980"
      ]
     },
     "execution_count": 53,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.describe()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 데이터 정렬\n",
    "- sort_values()\n",
    "- 특정 컬럼(열)을 기준으로 데이터를 정렬합니다."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 54,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>A</th>\n",
       "      <th>B</th>\n",
       "      <th>C</th>\n",
       "      <th>D</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>2021-01-01</th>\n",
       "      <td>0.549616</td>\n",
       "      <td>1.420946</td>\n",
       "      <td>-1.058392</td>\n",
       "      <td>0.910980</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2021-01-02</th>\n",
       "      <td>1.227611</td>\n",
       "      <td>0.796084</td>\n",
       "      <td>0.592796</td>\n",
       "      <td>-0.200915</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2021-01-03</th>\n",
       "      <td>-0.081290</td>\n",
       "      <td>0.850221</td>\n",
       "      <td>-0.418516</td>\n",
       "      <td>-0.205518</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2021-01-04</th>\n",
       "      <td>0.149968</td>\n",
       "      <td>0.533683</td>\n",
       "      <td>0.168538</td>\n",
       "      <td>-0.990762</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2021-01-05</th>\n",
       "      <td>2.526694</td>\n",
       "      <td>0.893960</td>\n",
       "      <td>-0.100311</td>\n",
       "      <td>0.009136</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2021-01-06</th>\n",
       "      <td>0.106058</td>\n",
       "      <td>-0.135166</td>\n",
       "      <td>0.377502</td>\n",
       "      <td>-0.854301</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                   A         B         C         D\n",
       "2021-01-01  0.549616  1.420946 -1.058392  0.910980\n",
       "2021-01-02  1.227611  0.796084  0.592796 -0.200915\n",
       "2021-01-03 -0.081290  0.850221 -0.418516 -0.205518\n",
       "2021-01-04  0.149968  0.533683  0.168538 -0.990762\n",
       "2021-01-05  2.526694  0.893960 -0.100311  0.009136\n",
       "2021-01-06  0.106058 -0.135166  0.377502 -0.854301"
      ]
     },
     "execution_count": 54,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 57,
   "metadata": {},
   "outputs": [],
   "source": [
    "df.sort_values(by='B', ascending=False, inplace=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 58,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>A</th>\n",
       "      <th>B</th>\n",
       "      <th>C</th>\n",
       "      <th>D</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>2021-01-01</th>\n",
       "      <td>0.549616</td>\n",
       "      <td>1.420946</td>\n",
       "      <td>-1.058392</td>\n",
       "      <td>0.910980</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2021-01-05</th>\n",
       "      <td>2.526694</td>\n",
       "      <td>0.893960</td>\n",
       "      <td>-0.100311</td>\n",
       "      <td>0.009136</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2021-01-03</th>\n",
       "      <td>-0.081290</td>\n",
       "      <td>0.850221</td>\n",
       "      <td>-0.418516</td>\n",
       "      <td>-0.205518</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2021-01-02</th>\n",
       "      <td>1.227611</td>\n",
       "      <td>0.796084</td>\n",
       "      <td>0.592796</td>\n",
       "      <td>-0.200915</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2021-01-04</th>\n",
       "      <td>0.149968</td>\n",
       "      <td>0.533683</td>\n",
       "      <td>0.168538</td>\n",
       "      <td>-0.990762</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2021-01-06</th>\n",
       "      <td>0.106058</td>\n",
       "      <td>-0.135166</td>\n",
       "      <td>0.377502</td>\n",
       "      <td>-0.854301</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                   A         B         C         D\n",
       "2021-01-01  0.549616  1.420946 -1.058392  0.910980\n",
       "2021-01-05  2.526694  0.893960 -0.100311  0.009136\n",
       "2021-01-03 -0.081290  0.850221 -0.418516 -0.205518\n",
       "2021-01-02  1.227611  0.796084  0.592796 -0.200915\n",
       "2021-01-04  0.149968  0.533683  0.168538 -0.990762\n",
       "2021-01-06  0.106058 -0.135166  0.377502 -0.854301"
      ]
     },
     "execution_count": 58,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "ascending=False : 내림차순 정렬  \n",
    "inplace=True : 수정값 저장"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 데이터 선택"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 59,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>A</th>\n",
       "      <th>B</th>\n",
       "      <th>C</th>\n",
       "      <th>D</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>2021-01-01</th>\n",
       "      <td>0.549616</td>\n",
       "      <td>1.420946</td>\n",
       "      <td>-1.058392</td>\n",
       "      <td>0.910980</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2021-01-05</th>\n",
       "      <td>2.526694</td>\n",
       "      <td>0.893960</td>\n",
       "      <td>-0.100311</td>\n",
       "      <td>0.009136</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2021-01-03</th>\n",
       "      <td>-0.081290</td>\n",
       "      <td>0.850221</td>\n",
       "      <td>-0.418516</td>\n",
       "      <td>-0.205518</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2021-01-02</th>\n",
       "      <td>1.227611</td>\n",
       "      <td>0.796084</td>\n",
       "      <td>0.592796</td>\n",
       "      <td>-0.200915</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2021-01-04</th>\n",
       "      <td>0.149968</td>\n",
       "      <td>0.533683</td>\n",
       "      <td>0.168538</td>\n",
       "      <td>-0.990762</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2021-01-06</th>\n",
       "      <td>0.106058</td>\n",
       "      <td>-0.135166</td>\n",
       "      <td>0.377502</td>\n",
       "      <td>-0.854301</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                   A         B         C         D\n",
       "2021-01-01  0.549616  1.420946 -1.058392  0.910980\n",
       "2021-01-05  2.526694  0.893960 -0.100311  0.009136\n",
       "2021-01-03 -0.081290  0.850221 -0.418516 -0.205518\n",
       "2021-01-02  1.227611  0.796084  0.592796 -0.200915\n",
       "2021-01-04  0.149968  0.533683  0.168538 -0.990762\n",
       "2021-01-06  0.106058 -0.135166  0.377502 -0.854301"
      ]
     },
     "execution_count": 59,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 60,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "2021-01-01    0.549616\n",
       "2021-01-05    2.526694\n",
       "2021-01-03   -0.081290\n",
       "2021-01-02    1.227611\n",
       "2021-01-04    0.149968\n",
       "2021-01-06    0.106058\n",
       "Name: A, dtype: float64"
      ]
     },
     "execution_count": 60,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# 한 개 컬럼 선택\n",
    "df['A']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 61,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "pandas.core.series.Series"
      ]
     },
     "execution_count": 61,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "type(df['A'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 62,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>A</th>\n",
       "      <th>B</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>2021-01-01</th>\n",
       "      <td>0.549616</td>\n",
       "      <td>1.420946</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2021-01-05</th>\n",
       "      <td>2.526694</td>\n",
       "      <td>0.893960</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2021-01-03</th>\n",
       "      <td>-0.081290</td>\n",
       "      <td>0.850221</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2021-01-02</th>\n",
       "      <td>1.227611</td>\n",
       "      <td>0.796084</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2021-01-04</th>\n",
       "      <td>0.149968</td>\n",
       "      <td>0.533683</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2021-01-06</th>\n",
       "      <td>0.106058</td>\n",
       "      <td>-0.135166</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                   A         B\n",
       "2021-01-01  0.549616  1.420946\n",
       "2021-01-05  2.526694  0.893960\n",
       "2021-01-03 -0.081290  0.850221\n",
       "2021-01-02  1.227611  0.796084\n",
       "2021-01-04  0.149968  0.533683\n",
       "2021-01-06  0.106058 -0.135166"
      ]
     },
     "execution_count": 62,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# 두개이상 컬럼 선택\n",
    "df[['A', 'B']]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "두개 이상의 경우 리스트에 담아서 해줘야 한다"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### offset index\n",
    "- [n:m] : n부터 m-1 까지\n",
    "- 인덱스나 컬럼의 이름으로 slice 하는 경우는 끝을 포함합니다."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 63,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>A</th>\n",
       "      <th>B</th>\n",
       "      <th>C</th>\n",
       "      <th>D</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>2021-01-01</th>\n",
       "      <td>0.549616</td>\n",
       "      <td>1.420946</td>\n",
       "      <td>-1.058392</td>\n",
       "      <td>0.910980</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2021-01-05</th>\n",
       "      <td>2.526694</td>\n",
       "      <td>0.893960</td>\n",
       "      <td>-0.100311</td>\n",
       "      <td>0.009136</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2021-01-03</th>\n",
       "      <td>-0.081290</td>\n",
       "      <td>0.850221</td>\n",
       "      <td>-0.418516</td>\n",
       "      <td>-0.205518</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2021-01-02</th>\n",
       "      <td>1.227611</td>\n",
       "      <td>0.796084</td>\n",
       "      <td>0.592796</td>\n",
       "      <td>-0.200915</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2021-01-04</th>\n",
       "      <td>0.149968</td>\n",
       "      <td>0.533683</td>\n",
       "      <td>0.168538</td>\n",
       "      <td>-0.990762</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2021-01-06</th>\n",
       "      <td>0.106058</td>\n",
       "      <td>-0.135166</td>\n",
       "      <td>0.377502</td>\n",
       "      <td>-0.854301</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                   A         B         C         D\n",
       "2021-01-01  0.549616  1.420946 -1.058392  0.910980\n",
       "2021-01-05  2.526694  0.893960 -0.100311  0.009136\n",
       "2021-01-03 -0.081290  0.850221 -0.418516 -0.205518\n",
       "2021-01-02  1.227611  0.796084  0.592796 -0.200915\n",
       "2021-01-04  0.149968  0.533683  0.168538 -0.990762\n",
       "2021-01-06  0.106058 -0.135166  0.377502 -0.854301"
      ]
     },
     "execution_count": 63,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 64,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>A</th>\n",
       "      <th>B</th>\n",
       "      <th>C</th>\n",
       "      <th>D</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>2021-01-01</th>\n",
       "      <td>0.549616</td>\n",
       "      <td>1.420946</td>\n",
       "      <td>-1.058392</td>\n",
       "      <td>0.910980</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2021-01-05</th>\n",
       "      <td>2.526694</td>\n",
       "      <td>0.893960</td>\n",
       "      <td>-0.100311</td>\n",
       "      <td>0.009136</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2021-01-03</th>\n",
       "      <td>-0.081290</td>\n",
       "      <td>0.850221</td>\n",
       "      <td>-0.418516</td>\n",
       "      <td>-0.205518</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                   A         B         C         D\n",
       "2021-01-01  0.549616  1.420946 -1.058392  0.910980\n",
       "2021-01-05  2.526694  0.893960 -0.100311  0.009136\n",
       "2021-01-03 -0.081290  0.850221 -0.418516 -0.205518"
      ]
     },
     "execution_count": 64,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df[0:3]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 65,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>A</th>\n",
       "      <th>B</th>\n",
       "      <th>C</th>\n",
       "      <th>D</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>2021-01-01</th>\n",
       "      <td>0.549616</td>\n",
       "      <td>1.420946</td>\n",
       "      <td>-1.058392</td>\n",
       "      <td>0.910980</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2021-01-03</th>\n",
       "      <td>-0.081290</td>\n",
       "      <td>0.850221</td>\n",
       "      <td>-0.418516</td>\n",
       "      <td>-0.205518</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2021-01-02</th>\n",
       "      <td>1.227611</td>\n",
       "      <td>0.796084</td>\n",
       "      <td>0.592796</td>\n",
       "      <td>-0.200915</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2021-01-04</th>\n",
       "      <td>0.149968</td>\n",
       "      <td>0.533683</td>\n",
       "      <td>0.168538</td>\n",
       "      <td>-0.990762</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                   A         B         C         D\n",
       "2021-01-01  0.549616  1.420946 -1.058392  0.910980\n",
       "2021-01-03 -0.081290  0.850221 -0.418516 -0.205518\n",
       "2021-01-02  1.227611  0.796084  0.592796 -0.200915\n",
       "2021-01-04  0.149968  0.533683  0.168538 -0.990762"
      ]
     },
     "execution_count": 65,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df['20210101':'20210104']"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "- loc : location\n",
    "- index 이름으로 특정 행, 열을 선택합니다."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 66,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>A</th>\n",
       "      <th>B</th>\n",
       "      <th>C</th>\n",
       "      <th>D</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>2021-01-01</th>\n",
       "      <td>0.549616</td>\n",
       "      <td>1.420946</td>\n",
       "      <td>-1.058392</td>\n",
       "      <td>0.910980</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2021-01-05</th>\n",
       "      <td>2.526694</td>\n",
       "      <td>0.893960</td>\n",
       "      <td>-0.100311</td>\n",
       "      <td>0.009136</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2021-01-03</th>\n",
       "      <td>-0.081290</td>\n",
       "      <td>0.850221</td>\n",
       "      <td>-0.418516</td>\n",
       "      <td>-0.205518</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2021-01-02</th>\n",
       "      <td>1.227611</td>\n",
       "      <td>0.796084</td>\n",
       "      <td>0.592796</td>\n",
       "      <td>-0.200915</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2021-01-04</th>\n",
       "      <td>0.149968</td>\n",
       "      <td>0.533683</td>\n",
       "      <td>0.168538</td>\n",
       "      <td>-0.990762</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2021-01-06</th>\n",
       "      <td>0.106058</td>\n",
       "      <td>-0.135166</td>\n",
       "      <td>0.377502</td>\n",
       "      <td>-0.854301</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                   A         B         C         D\n",
       "2021-01-01  0.549616  1.420946 -1.058392  0.910980\n",
       "2021-01-05  2.526694  0.893960 -0.100311  0.009136\n",
       "2021-01-03 -0.081290  0.850221 -0.418516 -0.205518\n",
       "2021-01-02  1.227611  0.796084  0.592796 -0.200915\n",
       "2021-01-04  0.149968  0.533683  0.168538 -0.990762\n",
       "2021-01-06  0.106058 -0.135166  0.377502 -0.854301"
      ]
     },
     "execution_count": 66,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 67,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>A</th>\n",
       "      <th>B</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>2021-01-01</th>\n",
       "      <td>0.549616</td>\n",
       "      <td>1.420946</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2021-01-05</th>\n",
       "      <td>2.526694</td>\n",
       "      <td>0.893960</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2021-01-03</th>\n",
       "      <td>-0.081290</td>\n",
       "      <td>0.850221</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2021-01-02</th>\n",
       "      <td>1.227611</td>\n",
       "      <td>0.796084</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2021-01-04</th>\n",
       "      <td>0.149968</td>\n",
       "      <td>0.533683</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2021-01-06</th>\n",
       "      <td>0.106058</td>\n",
       "      <td>-0.135166</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                   A         B\n",
       "2021-01-01  0.549616  1.420946\n",
       "2021-01-05  2.526694  0.893960\n",
       "2021-01-03 -0.081290  0.850221\n",
       "2021-01-02  1.227611  0.796084\n",
       "2021-01-04  0.149968  0.533683\n",
       "2021-01-06  0.106058 -0.135166"
      ]
     },
     "execution_count": 67,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.loc[:, ['A', 'B']]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    ": 이거는 앞에 인덱스는 전부 가져오라는 것이다.  \n",
    "['A', 'B'] 대괄호 안에 의미는 A, B 만 컬럼으로 가져와라 이다."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 70,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>A</th>\n",
       "      <th>D</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>2021-01-03</th>\n",
       "      <td>-0.081290</td>\n",
       "      <td>-0.205518</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2021-01-02</th>\n",
       "      <td>1.227611</td>\n",
       "      <td>-0.200915</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2021-01-04</th>\n",
       "      <td>0.149968</td>\n",
       "      <td>-0.990762</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                   A         D\n",
       "2021-01-03 -0.081290 -0.205518\n",
       "2021-01-02  1.227611 -0.200915\n",
       "2021-01-04  0.149968 -0.990762"
      ]
     },
     "execution_count": 70,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.loc['20210102':'20210104', ['A','D']]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 71,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>A</th>\n",
       "      <th>B</th>\n",
       "      <th>C</th>\n",
       "      <th>D</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>2021-01-03</th>\n",
       "      <td>-0.081290</td>\n",
       "      <td>0.850221</td>\n",
       "      <td>-0.418516</td>\n",
       "      <td>-0.205518</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2021-01-02</th>\n",
       "      <td>1.227611</td>\n",
       "      <td>0.796084</td>\n",
       "      <td>0.592796</td>\n",
       "      <td>-0.200915</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2021-01-04</th>\n",
       "      <td>0.149968</td>\n",
       "      <td>0.533683</td>\n",
       "      <td>0.168538</td>\n",
       "      <td>-0.990762</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                   A         B         C         D\n",
       "2021-01-03 -0.081290  0.850221 -0.418516 -0.205518\n",
       "2021-01-02  1.227611  0.796084  0.592796 -0.200915\n",
       "2021-01-04  0.149968  0.533683  0.168538 -0.990762"
      ]
     },
     "execution_count": 71,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.loc['20210102':'20210104', 'A':'D']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 72,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "A    1.227611\n",
       "B    0.796084\n",
       "Name: 2021-01-02 00:00:00, dtype: float64"
      ]
     },
     "execution_count": 72,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.loc['20210102', ['A','B']]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "- iloc : inter location  \n",
    "    - 컴퓨터가 인식하는 인덱스 값으로 선택 "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 73,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>A</th>\n",
       "      <th>B</th>\n",
       "      <th>C</th>\n",
       "      <th>D</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>2021-01-01</th>\n",
       "      <td>0.549616</td>\n",
       "      <td>1.420946</td>\n",
       "      <td>-1.058392</td>\n",
       "      <td>0.910980</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2021-01-05</th>\n",
       "      <td>2.526694</td>\n",
       "      <td>0.893960</td>\n",
       "      <td>-0.100311</td>\n",
       "      <td>0.009136</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2021-01-03</th>\n",
       "      <td>-0.081290</td>\n",
       "      <td>0.850221</td>\n",
       "      <td>-0.418516</td>\n",
       "      <td>-0.205518</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2021-01-02</th>\n",
       "      <td>1.227611</td>\n",
       "      <td>0.796084</td>\n",
       "      <td>0.592796</td>\n",
       "      <td>-0.200915</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2021-01-04</th>\n",
       "      <td>0.149968</td>\n",
       "      <td>0.533683</td>\n",
       "      <td>0.168538</td>\n",
       "      <td>-0.990762</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2021-01-06</th>\n",
       "      <td>0.106058</td>\n",
       "      <td>-0.135166</td>\n",
       "      <td>0.377502</td>\n",
       "      <td>-0.854301</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                   A         B         C         D\n",
       "2021-01-01  0.549616  1.420946 -1.058392  0.910980\n",
       "2021-01-05  2.526694  0.893960 -0.100311  0.009136\n",
       "2021-01-03 -0.081290  0.850221 -0.418516 -0.205518\n",
       "2021-01-02  1.227611  0.796084  0.592796 -0.200915\n",
       "2021-01-04  0.149968  0.533683  0.168538 -0.990762\n",
       "2021-01-06  0.106058 -0.135166  0.377502 -0.854301"
      ]
     },
     "execution_count": 73,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 74,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "A    1.227611\n",
       "B    0.796084\n",
       "C    0.592796\n",
       "D   -0.200915\n",
       "Name: 2021-01-02 00:00:00, dtype: float64"
      ]
     },
     "execution_count": 74,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.iloc[3]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 75,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.592795984077853"
      ]
     },
     "execution_count": 75,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.iloc[3,2]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 76,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>A</th>\n",
       "      <th>B</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>2021-01-02</th>\n",
       "      <td>1.227611</td>\n",
       "      <td>0.796084</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2021-01-04</th>\n",
       "      <td>0.149968</td>\n",
       "      <td>0.533683</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                   A         B\n",
       "2021-01-02  1.227611  0.796084\n",
       "2021-01-04  0.149968  0.533683"
      ]
     },
     "execution_count": 76,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.iloc[3:5, 0:2]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 77,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>A</th>\n",
       "      <th>C</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>2021-01-05</th>\n",
       "      <td>2.526694</td>\n",
       "      <td>-0.100311</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2021-01-03</th>\n",
       "      <td>-0.081290</td>\n",
       "      <td>-0.418516</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2021-01-04</th>\n",
       "      <td>0.149968</td>\n",
       "      <td>0.168538</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                   A         C\n",
       "2021-01-05  2.526694 -0.100311\n",
       "2021-01-03 -0.081290 -0.418516\n",
       "2021-01-04  0.149968  0.168538"
      ]
     },
     "execution_count": 77,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.iloc[[1,2, 4], [0,2]]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 78,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>B</th>\n",
       "      <th>C</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>2021-01-01</th>\n",
       "      <td>1.420946</td>\n",
       "      <td>-1.058392</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2021-01-05</th>\n",
       "      <td>0.893960</td>\n",
       "      <td>-0.100311</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2021-01-03</th>\n",
       "      <td>0.850221</td>\n",
       "      <td>-0.418516</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2021-01-02</th>\n",
       "      <td>0.796084</td>\n",
       "      <td>0.592796</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2021-01-04</th>\n",
       "      <td>0.533683</td>\n",
       "      <td>0.168538</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2021-01-06</th>\n",
       "      <td>-0.135166</td>\n",
       "      <td>0.377502</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                   B         C\n",
       "2021-01-01  1.420946 -1.058392\n",
       "2021-01-05  0.893960 -0.100311\n",
       "2021-01-03  0.850221 -0.418516\n",
       "2021-01-02  0.796084  0.592796\n",
       "2021-01-04  0.533683  0.168538\n",
       "2021-01-06 -0.135166  0.377502"
      ]
     },
     "execution_count": 78,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.iloc[:, 1:3]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### condition"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 79,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>A</th>\n",
       "      <th>B</th>\n",
       "      <th>C</th>\n",
       "      <th>D</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>2021-01-01</th>\n",
       "      <td>0.549616</td>\n",
       "      <td>1.420946</td>\n",
       "      <td>-1.058392</td>\n",
       "      <td>0.910980</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2021-01-05</th>\n",
       "      <td>2.526694</td>\n",
       "      <td>0.893960</td>\n",
       "      <td>-0.100311</td>\n",
       "      <td>0.009136</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2021-01-03</th>\n",
       "      <td>-0.081290</td>\n",
       "      <td>0.850221</td>\n",
       "      <td>-0.418516</td>\n",
       "      <td>-0.205518</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2021-01-02</th>\n",
       "      <td>1.227611</td>\n",
       "      <td>0.796084</td>\n",
       "      <td>0.592796</td>\n",
       "      <td>-0.200915</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2021-01-04</th>\n",
       "      <td>0.149968</td>\n",
       "      <td>0.533683</td>\n",
       "      <td>0.168538</td>\n",
       "      <td>-0.990762</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2021-01-06</th>\n",
       "      <td>0.106058</td>\n",
       "      <td>-0.135166</td>\n",
       "      <td>0.377502</td>\n",
       "      <td>-0.854301</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                   A         B         C         D\n",
       "2021-01-01  0.549616  1.420946 -1.058392  0.910980\n",
       "2021-01-05  2.526694  0.893960 -0.100311  0.009136\n",
       "2021-01-03 -0.081290  0.850221 -0.418516 -0.205518\n",
       "2021-01-02  1.227611  0.796084  0.592796 -0.200915\n",
       "2021-01-04  0.149968  0.533683  0.168538 -0.990762\n",
       "2021-01-06  0.106058 -0.135166  0.377502 -0.854301"
      ]
     },
     "execution_count": 79,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 80,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "2021-01-01     True\n",
       "2021-01-05     True\n",
       "2021-01-03    False\n",
       "2021-01-02     True\n",
       "2021-01-04     True\n",
       "2021-01-06     True\n",
       "Name: A, dtype: bool"
      ]
     },
     "execution_count": 80,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# A 컬럼에서 0보다 큰 숫자(양수)만 선택\n",
    "\n",
    "df['A'] > 0"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 81,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>A</th>\n",
       "      <th>B</th>\n",
       "      <th>C</th>\n",
       "      <th>D</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>2021-01-01</th>\n",
       "      <td>0.549616</td>\n",
       "      <td>1.420946</td>\n",
       "      <td>-1.058392</td>\n",
       "      <td>0.910980</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2021-01-05</th>\n",
       "      <td>2.526694</td>\n",
       "      <td>0.893960</td>\n",
       "      <td>-0.100311</td>\n",
       "      <td>0.009136</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2021-01-02</th>\n",
       "      <td>1.227611</td>\n",
       "      <td>0.796084</td>\n",
       "      <td>0.592796</td>\n",
       "      <td>-0.200915</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2021-01-04</th>\n",
       "      <td>0.149968</td>\n",
       "      <td>0.533683</td>\n",
       "      <td>0.168538</td>\n",
       "      <td>-0.990762</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2021-01-06</th>\n",
       "      <td>0.106058</td>\n",
       "      <td>-0.135166</td>\n",
       "      <td>0.377502</td>\n",
       "      <td>-0.854301</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                   A         B         C         D\n",
       "2021-01-01  0.549616  1.420946 -1.058392  0.910980\n",
       "2021-01-05  2.526694  0.893960 -0.100311  0.009136\n",
       "2021-01-02  1.227611  0.796084  0.592796 -0.200915\n",
       "2021-01-04  0.149968  0.533683  0.168538 -0.990762\n",
       "2021-01-06  0.106058 -0.135166  0.377502 -0.854301"
      ]
     },
     "execution_count": 81,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df[df['A'] > 0]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 82,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>A</th>\n",
       "      <th>B</th>\n",
       "      <th>C</th>\n",
       "      <th>D</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>2021-01-01</th>\n",
       "      <td>0.549616</td>\n",
       "      <td>1.420946</td>\n",
       "      <td>NaN</td>\n",
       "      <td>0.910980</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2021-01-05</th>\n",
       "      <td>2.526694</td>\n",
       "      <td>0.893960</td>\n",
       "      <td>NaN</td>\n",
       "      <td>0.009136</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2021-01-03</th>\n",
       "      <td>NaN</td>\n",
       "      <td>0.850221</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2021-01-02</th>\n",
       "      <td>1.227611</td>\n",
       "      <td>0.796084</td>\n",
       "      <td>0.592796</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2021-01-04</th>\n",
       "      <td>0.149968</td>\n",
       "      <td>0.533683</td>\n",
       "      <td>0.168538</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2021-01-06</th>\n",
       "      <td>0.106058</td>\n",
       "      <td>NaN</td>\n",
       "      <td>0.377502</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                   A         B         C         D\n",
       "2021-01-01  0.549616  1.420946       NaN  0.910980\n",
       "2021-01-05  2.526694  0.893960       NaN  0.009136\n",
       "2021-01-03       NaN  0.850221       NaN       NaN\n",
       "2021-01-02  1.227611  0.796084  0.592796       NaN\n",
       "2021-01-04  0.149968  0.533683  0.168538       NaN\n",
       "2021-01-06  0.106058       NaN  0.377502       NaN"
      ]
     },
     "execution_count": 82,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df[df > 0]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "- NaN : Not a Number"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 컬럼추가\n",
    "- 기존 컬럼이 없으면 추가\n",
    "- 기존 컬럼이 있으면 수정"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 84,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>A</th>\n",
       "      <th>B</th>\n",
       "      <th>C</th>\n",
       "      <th>D</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>2021-01-01</th>\n",
       "      <td>0.549616</td>\n",
       "      <td>1.420946</td>\n",
       "      <td>-1.058392</td>\n",
       "      <td>0.910980</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2021-01-05</th>\n",
       "      <td>2.526694</td>\n",
       "      <td>0.893960</td>\n",
       "      <td>-0.100311</td>\n",
       "      <td>0.009136</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2021-01-03</th>\n",
       "      <td>-0.081290</td>\n",
       "      <td>0.850221</td>\n",
       "      <td>-0.418516</td>\n",
       "      <td>-0.205518</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2021-01-02</th>\n",
       "      <td>1.227611</td>\n",
       "      <td>0.796084</td>\n",
       "      <td>0.592796</td>\n",
       "      <td>-0.200915</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2021-01-04</th>\n",
       "      <td>0.149968</td>\n",
       "      <td>0.533683</td>\n",
       "      <td>0.168538</td>\n",
       "      <td>-0.990762</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2021-01-06</th>\n",
       "      <td>0.106058</td>\n",
       "      <td>-0.135166</td>\n",
       "      <td>0.377502</td>\n",
       "      <td>-0.854301</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                   A         B         C         D\n",
       "2021-01-01  0.549616  1.420946 -1.058392  0.910980\n",
       "2021-01-05  2.526694  0.893960 -0.100311  0.009136\n",
       "2021-01-03 -0.081290  0.850221 -0.418516 -0.205518\n",
       "2021-01-02  1.227611  0.796084  0.592796 -0.200915\n",
       "2021-01-04  0.149968  0.533683  0.168538 -0.990762\n",
       "2021-01-06  0.106058 -0.135166  0.377502 -0.854301"
      ]
     },
     "execution_count": 84,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 90,
   "metadata": {},
   "outputs": [],
   "source": [
    "df['E'] = ['one', 'one', 'two', 'three', 'four', 'five']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 86,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>A</th>\n",
       "      <th>B</th>\n",
       "      <th>C</th>\n",
       "      <th>D</th>\n",
       "      <th>E</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>2021-01-01</th>\n",
       "      <td>0.549616</td>\n",
       "      <td>1.420946</td>\n",
       "      <td>-1.058392</td>\n",
       "      <td>0.910980</td>\n",
       "      <td>one</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2021-01-05</th>\n",
       "      <td>2.526694</td>\n",
       "      <td>0.893960</td>\n",
       "      <td>-0.100311</td>\n",
       "      <td>0.009136</td>\n",
       "      <td>one</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2021-01-03</th>\n",
       "      <td>-0.081290</td>\n",
       "      <td>0.850221</td>\n",
       "      <td>-0.418516</td>\n",
       "      <td>-0.205518</td>\n",
       "      <td>two</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2021-01-02</th>\n",
       "      <td>1.227611</td>\n",
       "      <td>0.796084</td>\n",
       "      <td>0.592796</td>\n",
       "      <td>-0.200915</td>\n",
       "      <td>tree</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2021-01-04</th>\n",
       "      <td>0.149968</td>\n",
       "      <td>0.533683</td>\n",
       "      <td>0.168538</td>\n",
       "      <td>-0.990762</td>\n",
       "      <td>four</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2021-01-06</th>\n",
       "      <td>0.106058</td>\n",
       "      <td>-0.135166</td>\n",
       "      <td>0.377502</td>\n",
       "      <td>-0.854301</td>\n",
       "      <td>five</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                   A         B         C         D     E\n",
       "2021-01-01  0.549616  1.420946 -1.058392  0.910980   one\n",
       "2021-01-05  2.526694  0.893960 -0.100311  0.009136   one\n",
       "2021-01-03 -0.081290  0.850221 -0.418516 -0.205518   two\n",
       "2021-01-02  1.227611  0.796084  0.592796 -0.200915  tree\n",
       "2021-01-04  0.149968  0.533683  0.168538 -0.990762  four\n",
       "2021-01-06  0.106058 -0.135166  0.377502 -0.854301  five"
      ]
     },
     "execution_count": 86,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "- isin()\n",
    "- 특정 요소가 있는지 확인"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 91,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "2021-01-01    False\n",
       "2021-01-05    False\n",
       "2021-01-03     True\n",
       "2021-01-02    False\n",
       "2021-01-04    False\n",
       "2021-01-06    False\n",
       "Name: E, dtype: bool"
      ]
     },
     "execution_count": 91,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df['E'].isin(['two'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 92,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "2021-01-01    False\n",
       "2021-01-05    False\n",
       "2021-01-03     True\n",
       "2021-01-02    False\n",
       "2021-01-04    False\n",
       "2021-01-06     True\n",
       "Name: E, dtype: bool"
      ]
     },
     "execution_count": 92,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df['E'].isin(['two', 'five'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 93,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>A</th>\n",
       "      <th>B</th>\n",
       "      <th>C</th>\n",
       "      <th>D</th>\n",
       "      <th>E</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>2021-01-03</th>\n",
       "      <td>-0.081290</td>\n",
       "      <td>0.850221</td>\n",
       "      <td>-0.418516</td>\n",
       "      <td>-0.205518</td>\n",
       "      <td>two</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2021-01-02</th>\n",
       "      <td>1.227611</td>\n",
       "      <td>0.796084</td>\n",
       "      <td>0.592796</td>\n",
       "      <td>-0.200915</td>\n",
       "      <td>three</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2021-01-06</th>\n",
       "      <td>0.106058</td>\n",
       "      <td>-0.135166</td>\n",
       "      <td>0.377502</td>\n",
       "      <td>-0.854301</td>\n",
       "      <td>five</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                   A         B         C         D      E\n",
       "2021-01-03 -0.081290  0.850221 -0.418516 -0.205518    two\n",
       "2021-01-02  1.227611  0.796084  0.592796 -0.200915  three\n",
       "2021-01-06  0.106058 -0.135166  0.377502 -0.854301   five"
      ]
     },
     "execution_count": 93,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df[df['E'].isin(['two', 'five', 'three'])]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 특정 컬럼 제거\n",
    "- del\n",
    "- drop"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 94,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>A</th>\n",
       "      <th>B</th>\n",
       "      <th>C</th>\n",
       "      <th>D</th>\n",
       "      <th>E</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>2021-01-01</th>\n",
       "      <td>0.549616</td>\n",
       "      <td>1.420946</td>\n",
       "      <td>-1.058392</td>\n",
       "      <td>0.910980</td>\n",
       "      <td>one</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2021-01-05</th>\n",
       "      <td>2.526694</td>\n",
       "      <td>0.893960</td>\n",
       "      <td>-0.100311</td>\n",
       "      <td>0.009136</td>\n",
       "      <td>one</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2021-01-03</th>\n",
       "      <td>-0.081290</td>\n",
       "      <td>0.850221</td>\n",
       "      <td>-0.418516</td>\n",
       "      <td>-0.205518</td>\n",
       "      <td>two</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2021-01-02</th>\n",
       "      <td>1.227611</td>\n",
       "      <td>0.796084</td>\n",
       "      <td>0.592796</td>\n",
       "      <td>-0.200915</td>\n",
       "      <td>three</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2021-01-04</th>\n",
       "      <td>0.149968</td>\n",
       "      <td>0.533683</td>\n",
       "      <td>0.168538</td>\n",
       "      <td>-0.990762</td>\n",
       "      <td>four</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2021-01-06</th>\n",
       "      <td>0.106058</td>\n",
       "      <td>-0.135166</td>\n",
       "      <td>0.377502</td>\n",
       "      <td>-0.854301</td>\n",
       "      <td>five</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                   A         B         C         D      E\n",
       "2021-01-01  0.549616  1.420946 -1.058392  0.910980    one\n",
       "2021-01-05  2.526694  0.893960 -0.100311  0.009136    one\n",
       "2021-01-03 -0.081290  0.850221 -0.418516 -0.205518    two\n",
       "2021-01-02  1.227611  0.796084  0.592796 -0.200915  three\n",
       "2021-01-04  0.149968  0.533683  0.168538 -0.990762   four\n",
       "2021-01-06  0.106058 -0.135166  0.377502 -0.854301   five"
      ]
     },
     "execution_count": 94,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 95,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>A</th>\n",
       "      <th>B</th>\n",
       "      <th>C</th>\n",
       "      <th>D</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>2021-01-01</th>\n",
       "      <td>0.549616</td>\n",
       "      <td>1.420946</td>\n",
       "      <td>-1.058392</td>\n",
       "      <td>0.910980</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2021-01-05</th>\n",
       "      <td>2.526694</td>\n",
       "      <td>0.893960</td>\n",
       "      <td>-0.100311</td>\n",
       "      <td>0.009136</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2021-01-03</th>\n",
       "      <td>-0.081290</td>\n",
       "      <td>0.850221</td>\n",
       "      <td>-0.418516</td>\n",
       "      <td>-0.205518</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2021-01-02</th>\n",
       "      <td>1.227611</td>\n",
       "      <td>0.796084</td>\n",
       "      <td>0.592796</td>\n",
       "      <td>-0.200915</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2021-01-04</th>\n",
       "      <td>0.149968</td>\n",
       "      <td>0.533683</td>\n",
       "      <td>0.168538</td>\n",
       "      <td>-0.990762</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2021-01-06</th>\n",
       "      <td>0.106058</td>\n",
       "      <td>-0.135166</td>\n",
       "      <td>0.377502</td>\n",
       "      <td>-0.854301</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                   A         B         C         D\n",
       "2021-01-01  0.549616  1.420946 -1.058392  0.910980\n",
       "2021-01-05  2.526694  0.893960 -0.100311  0.009136\n",
       "2021-01-03 -0.081290  0.850221 -0.418516 -0.205518\n",
       "2021-01-02  1.227611  0.796084  0.592796 -0.200915\n",
       "2021-01-04  0.149968  0.533683  0.168538 -0.990762\n",
       "2021-01-06  0.106058 -0.135166  0.377502 -0.854301"
      ]
     },
     "execution_count": 95,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "del df['E']\n",
    "df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 97,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>A</th>\n",
       "      <th>B</th>\n",
       "      <th>C</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>2021-01-01</th>\n",
       "      <td>0.549616</td>\n",
       "      <td>1.420946</td>\n",
       "      <td>-1.058392</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2021-01-05</th>\n",
       "      <td>2.526694</td>\n",
       "      <td>0.893960</td>\n",
       "      <td>-0.100311</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2021-01-03</th>\n",
       "      <td>-0.081290</td>\n",
       "      <td>0.850221</td>\n",
       "      <td>-0.418516</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2021-01-02</th>\n",
       "      <td>1.227611</td>\n",
       "      <td>0.796084</td>\n",
       "      <td>0.592796</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2021-01-04</th>\n",
       "      <td>0.149968</td>\n",
       "      <td>0.533683</td>\n",
       "      <td>0.168538</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2021-01-06</th>\n",
       "      <td>0.106058</td>\n",
       "      <td>-0.135166</td>\n",
       "      <td>0.377502</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                   A         B         C\n",
       "2021-01-01  0.549616  1.420946 -1.058392\n",
       "2021-01-05  2.526694  0.893960 -0.100311\n",
       "2021-01-03 -0.081290  0.850221 -0.418516\n",
       "2021-01-02  1.227611  0.796084  0.592796\n",
       "2021-01-04  0.149968  0.533683  0.168538\n",
       "2021-01-06  0.106058 -0.135166  0.377502"
      ]
     },
     "execution_count": 97,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.drop(['D'], axis=1) # axis = 0 가로, asix = 1 세로"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 98,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>A</th>\n",
       "      <th>B</th>\n",
       "      <th>C</th>\n",
       "      <th>D</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>2021-01-01</th>\n",
       "      <td>0.549616</td>\n",
       "      <td>1.420946</td>\n",
       "      <td>-1.058392</td>\n",
       "      <td>0.910980</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2021-01-05</th>\n",
       "      <td>2.526694</td>\n",
       "      <td>0.893960</td>\n",
       "      <td>-0.100311</td>\n",
       "      <td>0.009136</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2021-01-03</th>\n",
       "      <td>-0.081290</td>\n",
       "      <td>0.850221</td>\n",
       "      <td>-0.418516</td>\n",
       "      <td>-0.205518</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2021-01-02</th>\n",
       "      <td>1.227611</td>\n",
       "      <td>0.796084</td>\n",
       "      <td>0.592796</td>\n",
       "      <td>-0.200915</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2021-01-06</th>\n",
       "      <td>0.106058</td>\n",
       "      <td>-0.135166</td>\n",
       "      <td>0.377502</td>\n",
       "      <td>-0.854301</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                   A         B         C         D\n",
       "2021-01-01  0.549616  1.420946 -1.058392  0.910980\n",
       "2021-01-05  2.526694  0.893960 -0.100311  0.009136\n",
       "2021-01-03 -0.081290  0.850221 -0.418516 -0.205518\n",
       "2021-01-02  1.227611  0.796084  0.592796 -0.200915\n",
       "2021-01-06  0.106058 -0.135166  0.377502 -0.854301"
      ]
     },
     "execution_count": 98,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.drop(['20210104'])"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### apply()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 99,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>A</th>\n",
       "      <th>B</th>\n",
       "      <th>C</th>\n",
       "      <th>D</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>2021-01-01</th>\n",
       "      <td>0.549616</td>\n",
       "      <td>1.420946</td>\n",
       "      <td>-1.058392</td>\n",
       "      <td>0.910980</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2021-01-05</th>\n",
       "      <td>2.526694</td>\n",
       "      <td>0.893960</td>\n",
       "      <td>-0.100311</td>\n",
       "      <td>0.009136</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2021-01-03</th>\n",
       "      <td>-0.081290</td>\n",
       "      <td>0.850221</td>\n",
       "      <td>-0.418516</td>\n",
       "      <td>-0.205518</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2021-01-02</th>\n",
       "      <td>1.227611</td>\n",
       "      <td>0.796084</td>\n",
       "      <td>0.592796</td>\n",
       "      <td>-0.200915</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2021-01-04</th>\n",
       "      <td>0.149968</td>\n",
       "      <td>0.533683</td>\n",
       "      <td>0.168538</td>\n",
       "      <td>-0.990762</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2021-01-06</th>\n",
       "      <td>0.106058</td>\n",
       "      <td>-0.135166</td>\n",
       "      <td>0.377502</td>\n",
       "      <td>-0.854301</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                   A         B         C         D\n",
       "2021-01-01  0.549616  1.420946 -1.058392  0.910980\n",
       "2021-01-05  2.526694  0.893960 -0.100311  0.009136\n",
       "2021-01-03 -0.081290  0.850221 -0.418516 -0.205518\n",
       "2021-01-02  1.227611  0.796084  0.592796 -0.200915\n",
       "2021-01-04  0.149968  0.533683  0.168538 -0.990762\n",
       "2021-01-06  0.106058 -0.135166  0.377502 -0.854301"
      ]
     },
     "execution_count": 99,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 100,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "4.478656676266542"
      ]
     },
     "execution_count": 100,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df['A'].apply('sum')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 101,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.746442779377757"
      ]
     },
     "execution_count": 101,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df['A'].apply('mean')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 102,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(-0.08129008930424873, 2.5266941068572555)"
      ]
     },
     "execution_count": 102,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df['A'].apply('min'), df['A'].apply('max')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 104,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "A    4.478657\n",
       "B    4.359729\n",
       "dtype: float64"
      ]
     },
     "execution_count": 104,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df[['A', 'B']].apply('sum')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 105,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "2021-01-01    0.549616\n",
       "2021-01-05    2.526694\n",
       "2021-01-03   -0.081290\n",
       "2021-01-02    1.227611\n",
       "2021-01-04    0.149968\n",
       "2021-01-06    0.106058\n",
       "Name: A, dtype: float64"
      ]
     },
     "execution_count": 105,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df['A'].apply(np.sum)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 106,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "2021-01-01    0.549616\n",
       "2021-01-05    2.526694\n",
       "2021-01-03   -0.081290\n",
       "2021-01-02    1.227611\n",
       "2021-01-04    0.149968\n",
       "2021-01-06    0.106058\n",
       "Name: A, dtype: float64"
      ]
     },
     "execution_count": 106,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df['A'].apply(np.mean)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 107,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>A</th>\n",
       "      <th>B</th>\n",
       "      <th>C</th>\n",
       "      <th>D</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>2021-01-01</th>\n",
       "      <td>0.549616</td>\n",
       "      <td>1.420946</td>\n",
       "      <td>-1.058392</td>\n",
       "      <td>0.910980</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2021-01-05</th>\n",
       "      <td>2.526694</td>\n",
       "      <td>0.893960</td>\n",
       "      <td>-0.100311</td>\n",
       "      <td>0.009136</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2021-01-03</th>\n",
       "      <td>-0.081290</td>\n",
       "      <td>0.850221</td>\n",
       "      <td>-0.418516</td>\n",
       "      <td>-0.205518</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2021-01-02</th>\n",
       "      <td>1.227611</td>\n",
       "      <td>0.796084</td>\n",
       "      <td>0.592796</td>\n",
       "      <td>-0.200915</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2021-01-04</th>\n",
       "      <td>0.149968</td>\n",
       "      <td>0.533683</td>\n",
       "      <td>0.168538</td>\n",
       "      <td>-0.990762</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2021-01-06</th>\n",
       "      <td>0.106058</td>\n",
       "      <td>-0.135166</td>\n",
       "      <td>0.377502</td>\n",
       "      <td>-0.854301</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                   A         B         C         D\n",
       "2021-01-01  0.549616  1.420946 -1.058392  0.910980\n",
       "2021-01-05  2.526694  0.893960 -0.100311  0.009136\n",
       "2021-01-03 -0.081290  0.850221 -0.418516 -0.205518\n",
       "2021-01-02  1.227611  0.796084  0.592796 -0.200915\n",
       "2021-01-04  0.149968  0.533683  0.168538 -0.990762\n",
       "2021-01-06  0.106058 -0.135166  0.377502 -0.854301"
      ]
     },
     "execution_count": 107,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 108,
   "metadata": {},
   "outputs": [],
   "source": [
    "def plusminus(num):\n",
    "    return 'Plus' if num > 0 else 'minus'\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 109,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "2021-01-01     Plus\n",
       "2021-01-05     Plus\n",
       "2021-01-03    minus\n",
       "2021-01-02     Plus\n",
       "2021-01-04     Plus\n",
       "2021-01-06     Plus\n",
       "Name: A, dtype: object"
      ]
     },
     "execution_count": 109,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df['A'].apply(plusminus)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 110,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "2021-01-01     plus\n",
       "2021-01-05     plus\n",
       "2021-01-03    minus\n",
       "2021-01-02     plus\n",
       "2021-01-04     plus\n",
       "2021-01-06     plus\n",
       "Name: A, dtype: object"
      ]
     },
     "execution_count": 110,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df['A'].apply(lambda num: 'plus' if num > 0 else 'minus')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "---"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 2.cctv 데이터 훑어보기"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 111,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>구별</th>\n",
       "      <th>소계</th>\n",
       "      <th>2013년도 이전</th>\n",
       "      <th>2014년</th>\n",
       "      <th>2015년</th>\n",
       "      <th>2016년</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>강남구</td>\n",
       "      <td>3238</td>\n",
       "      <td>1292</td>\n",
       "      <td>430</td>\n",
       "      <td>584</td>\n",
       "      <td>932</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>강동구</td>\n",
       "      <td>1010</td>\n",
       "      <td>379</td>\n",
       "      <td>99</td>\n",
       "      <td>155</td>\n",
       "      <td>377</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>강북구</td>\n",
       "      <td>831</td>\n",
       "      <td>369</td>\n",
       "      <td>120</td>\n",
       "      <td>138</td>\n",
       "      <td>204</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>강서구</td>\n",
       "      <td>911</td>\n",
       "      <td>388</td>\n",
       "      <td>258</td>\n",
       "      <td>184</td>\n",
       "      <td>81</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>관악구</td>\n",
       "      <td>2109</td>\n",
       "      <td>846</td>\n",
       "      <td>260</td>\n",
       "      <td>390</td>\n",
       "      <td>613</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "    구별    소계  2013년도 이전  2014년  2015년  2016년\n",
       "0  강남구  3238       1292    430    584    932\n",
       "1  강동구  1010        379     99    155    377\n",
       "2  강북구   831        369    120    138    204\n",
       "3  강서구   911        388    258    184     81\n",
       "4  관악구  2109        846    260    390    613"
      ]
     },
     "execution_count": 111,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "CCTV_Seoul.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 112,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>구별</th>\n",
       "      <th>소계</th>\n",
       "      <th>2013년도 이전</th>\n",
       "      <th>2014년</th>\n",
       "      <th>2015년</th>\n",
       "      <th>2016년</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>20</th>\n",
       "      <td>용산구</td>\n",
       "      <td>2096</td>\n",
       "      <td>1368</td>\n",
       "      <td>218</td>\n",
       "      <td>112</td>\n",
       "      <td>398</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>21</th>\n",
       "      <td>은평구</td>\n",
       "      <td>2108</td>\n",
       "      <td>1138</td>\n",
       "      <td>224</td>\n",
       "      <td>278</td>\n",
       "      <td>468</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>22</th>\n",
       "      <td>종로구</td>\n",
       "      <td>1619</td>\n",
       "      <td>464</td>\n",
       "      <td>314</td>\n",
       "      <td>211</td>\n",
       "      <td>630</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>23</th>\n",
       "      <td>중구</td>\n",
       "      <td>1023</td>\n",
       "      <td>413</td>\n",
       "      <td>190</td>\n",
       "      <td>72</td>\n",
       "      <td>348</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>24</th>\n",
       "      <td>중랑구</td>\n",
       "      <td>916</td>\n",
       "      <td>509</td>\n",
       "      <td>121</td>\n",
       "      <td>177</td>\n",
       "      <td>109</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "     구별    소계  2013년도 이전  2014년  2015년  2016년\n",
       "20  용산구  2096       1368    218    112    398\n",
       "21  은평구  2108       1138    224    278    468\n",
       "22  종로구  1619        464    314    211    630\n",
       "23   중구  1023        413    190     72    348\n",
       "24  중랑구   916        509    121    177    109"
      ]
     },
     "execution_count": 112,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "CCTV_Seoul.tail()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 113,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>구별</th>\n",
       "      <th>소계</th>\n",
       "      <th>2013년도 이전</th>\n",
       "      <th>2014년</th>\n",
       "      <th>2015년</th>\n",
       "      <th>2016년</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>9</th>\n",
       "      <td>도봉구</td>\n",
       "      <td>825</td>\n",
       "      <td>238</td>\n",
       "      <td>159</td>\n",
       "      <td>42</td>\n",
       "      <td>386</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>강북구</td>\n",
       "      <td>831</td>\n",
       "      <td>369</td>\n",
       "      <td>120</td>\n",
       "      <td>138</td>\n",
       "      <td>204</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>광진구</td>\n",
       "      <td>878</td>\n",
       "      <td>573</td>\n",
       "      <td>78</td>\n",
       "      <td>53</td>\n",
       "      <td>174</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>강서구</td>\n",
       "      <td>911</td>\n",
       "      <td>388</td>\n",
       "      <td>258</td>\n",
       "      <td>184</td>\n",
       "      <td>81</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>24</th>\n",
       "      <td>중랑구</td>\n",
       "      <td>916</td>\n",
       "      <td>509</td>\n",
       "      <td>121</td>\n",
       "      <td>177</td>\n",
       "      <td>109</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "     구별   소계  2013년도 이전  2014년  2015년  2016년\n",
       "9   도봉구  825        238    159     42    386\n",
       "2   강북구  831        369    120    138    204\n",
       "5   광진구  878        573     78     53    174\n",
       "3   강서구  911        388    258    184     81\n",
       "24  중랑구  916        509    121    177    109"
      ]
     },
     "execution_count": 113,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "CCTV_Seoul.sort_values(by='소계',ascending=True).head(5)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 114,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>구별</th>\n",
       "      <th>소계</th>\n",
       "      <th>2013년도 이전</th>\n",
       "      <th>2014년</th>\n",
       "      <th>2015년</th>\n",
       "      <th>2016년</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>강남구</td>\n",
       "      <td>3238</td>\n",
       "      <td>1292</td>\n",
       "      <td>430</td>\n",
       "      <td>584</td>\n",
       "      <td>932</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>18</th>\n",
       "      <td>양천구</td>\n",
       "      <td>2482</td>\n",
       "      <td>1843</td>\n",
       "      <td>142</td>\n",
       "      <td>30</td>\n",
       "      <td>467</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>14</th>\n",
       "      <td>서초구</td>\n",
       "      <td>2297</td>\n",
       "      <td>1406</td>\n",
       "      <td>157</td>\n",
       "      <td>336</td>\n",
       "      <td>398</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>관악구</td>\n",
       "      <td>2109</td>\n",
       "      <td>846</td>\n",
       "      <td>260</td>\n",
       "      <td>390</td>\n",
       "      <td>613</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>21</th>\n",
       "      <td>은평구</td>\n",
       "      <td>2108</td>\n",
       "      <td>1138</td>\n",
       "      <td>224</td>\n",
       "      <td>278</td>\n",
       "      <td>468</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "     구별    소계  2013년도 이전  2014년  2015년  2016년\n",
       "0   강남구  3238       1292    430    584    932\n",
       "18  양천구  2482       1843    142     30    467\n",
       "14  서초구  2297       1406    157    336    398\n",
       "4   관악구  2109        846    260    390    613\n",
       "21  은평구  2108       1138    224    278    468"
      ]
     },
     "execution_count": 114,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "CCTV_Seoul.sort_values(by='소계',ascending=False).head(5)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 117,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>구별</th>\n",
       "      <th>소계</th>\n",
       "      <th>2013년도 이전</th>\n",
       "      <th>2014년</th>\n",
       "      <th>2015년</th>\n",
       "      <th>2016년</th>\n",
       "      <th>최근증가율</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>22</th>\n",
       "      <td>종로구</td>\n",
       "      <td>1619</td>\n",
       "      <td>464</td>\n",
       "      <td>314</td>\n",
       "      <td>211</td>\n",
       "      <td>630</td>\n",
       "      <td>248.922414</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9</th>\n",
       "      <td>도봉구</td>\n",
       "      <td>825</td>\n",
       "      <td>238</td>\n",
       "      <td>159</td>\n",
       "      <td>42</td>\n",
       "      <td>386</td>\n",
       "      <td>246.638655</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>12</th>\n",
       "      <td>마포구</td>\n",
       "      <td>980</td>\n",
       "      <td>314</td>\n",
       "      <td>118</td>\n",
       "      <td>169</td>\n",
       "      <td>379</td>\n",
       "      <td>212.101911</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>노원구</td>\n",
       "      <td>1566</td>\n",
       "      <td>542</td>\n",
       "      <td>57</td>\n",
       "      <td>451</td>\n",
       "      <td>516</td>\n",
       "      <td>188.929889</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>강동구</td>\n",
       "      <td>1010</td>\n",
       "      <td>379</td>\n",
       "      <td>99</td>\n",
       "      <td>155</td>\n",
       "      <td>377</td>\n",
       "      <td>166.490765</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "     구별    소계  2013년도 이전  2014년  2015년  2016년       최근증가율\n",
       "22  종로구  1619        464    314    211    630  248.922414\n",
       "9   도봉구   825        238    159     42    386  246.638655\n",
       "12  마포구   980        314    118    169    379  212.101911\n",
       "8   노원구  1566        542     57    451    516  188.929889\n",
       "1   강동구  1010        379     99    155    377  166.490765"
      ]
     },
     "execution_count": 117,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "CCTV_Seoul['최근증가율'] = (\n",
    "    (CCTV_Seoul['2016년'] + CCTV_Seoul['2015년'] + CCTV_Seoul['2014년']) / CCTV_Seoul['2013년도 이전'] *100\n",
    ")\n",
    "CCTV_Seoul.sort_values(by='최근증가율', ascending=False).head(5)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 3.인구현황 데이터 훑어보기"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 126,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>자치구</th>\n",
       "      <th>계</th>\n",
       "      <th>계.1</th>\n",
       "      <th>계.2</th>\n",
       "      <th>65세이상고령자</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>종로구</td>\n",
       "      <td>164257</td>\n",
       "      <td>154770</td>\n",
       "      <td>9487</td>\n",
       "      <td>26182</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>중구</td>\n",
       "      <td>134593</td>\n",
       "      <td>125709</td>\n",
       "      <td>8884</td>\n",
       "      <td>21384</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>용산구</td>\n",
       "      <td>244444</td>\n",
       "      <td>229161</td>\n",
       "      <td>15283</td>\n",
       "      <td>36882</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>성동구</td>\n",
       "      <td>312711</td>\n",
       "      <td>304808</td>\n",
       "      <td>7903</td>\n",
       "      <td>41273</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>광진구</td>\n",
       "      <td>372298</td>\n",
       "      <td>357703</td>\n",
       "      <td>14595</td>\n",
       "      <td>43953</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   자치구       계     계.1    계.2  65세이상고령자\n",
       "1  종로구  164257  154770   9487     26182\n",
       "2   중구  134593  125709   8884     21384\n",
       "3  용산구  244444  229161  15283     36882\n",
       "4  성동구  312711  304808   7903     41273\n",
       "5  광진구  372298  357703  14595     43953"
      ]
     },
     "execution_count": 126,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "pop_Seoul.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 127,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>자치구</th>\n",
       "      <th>계</th>\n",
       "      <th>계.1</th>\n",
       "      <th>계.2</th>\n",
       "      <th>65세이상고령자</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>21</th>\n",
       "      <td>관악구</td>\n",
       "      <td>520929</td>\n",
       "      <td>503297</td>\n",
       "      <td>17632</td>\n",
       "      <td>70046</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>22</th>\n",
       "      <td>서초구</td>\n",
       "      <td>445401</td>\n",
       "      <td>441102</td>\n",
       "      <td>4299</td>\n",
       "      <td>53205</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>23</th>\n",
       "      <td>강남구</td>\n",
       "      <td>561052</td>\n",
       "      <td>556164</td>\n",
       "      <td>4888</td>\n",
       "      <td>65060</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>24</th>\n",
       "      <td>송파구</td>\n",
       "      <td>671173</td>\n",
       "      <td>664496</td>\n",
       "      <td>6677</td>\n",
       "      <td>76582</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25</th>\n",
       "      <td>강동구</td>\n",
       "      <td>440359</td>\n",
       "      <td>436223</td>\n",
       "      <td>4136</td>\n",
       "      <td>56161</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "    자치구       계     계.1    계.2  65세이상고령자\n",
       "21  관악구  520929  503297  17632     70046\n",
       "22  서초구  445401  441102   4299     53205\n",
       "23  강남구  561052  556164   4888     65060\n",
       "24  송파구  671173  664496   6677     76582\n",
       "25  강동구  440359  436223   4136     56161"
      ]
     },
     "execution_count": 127,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "pop_Seoul.tail()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 129,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>자치구</th>\n",
       "      <th>계</th>\n",
       "      <th>계.1</th>\n",
       "      <th>계.2</th>\n",
       "      <th>65세이상고령자</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>중구</td>\n",
       "      <td>134593</td>\n",
       "      <td>125709</td>\n",
       "      <td>8884</td>\n",
       "      <td>21384</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>용산구</td>\n",
       "      <td>244444</td>\n",
       "      <td>229161</td>\n",
       "      <td>15283</td>\n",
       "      <td>36882</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>성동구</td>\n",
       "      <td>312711</td>\n",
       "      <td>304808</td>\n",
       "      <td>7903</td>\n",
       "      <td>41273</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>광진구</td>\n",
       "      <td>372298</td>\n",
       "      <td>357703</td>\n",
       "      <td>14595</td>\n",
       "      <td>43953</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>동대문구</td>\n",
       "      <td>366011</td>\n",
       "      <td>350647</td>\n",
       "      <td>15364</td>\n",
       "      <td>55718</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "    자치구       계     계.1    계.2  65세이상고령자\n",
       "2    중구  134593  125709   8884     21384\n",
       "3   용산구  244444  229161  15283     36882\n",
       "4   성동구  312711  304808   7903     41273\n",
       "5   광진구  372298  357703  14595     43953\n",
       "6  동대문구  366011  350647  15364     55718"
      ]
     },
     "execution_count": 129,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "pop_Seoul.drop([1], axis=0, inplace=True)\n",
    "pop_Seoul.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 131,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array(['중구', '용산구', '성동구', '광진구', '동대문구', '중랑구', '성북구', '강북구', '도봉구',\n",
       "       '노원구', '은평구', '서대문구', '마포구', '양천구', '강서구', '구로구', '금천구', '영등포구',\n",
       "       '동작구', '관악구', '서초구', '강남구', '송파구', '강동구'], dtype=object)"
      ]
     },
     "execution_count": 131,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "pop_Seoul['자치구'].unique()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 132,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "24"
      ]
     },
     "execution_count": 132,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "len(pop_Seoul['자치구'].unique())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 166,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>구별</th>\n",
       "      <th>인구수</th>\n",
       "      <th>한국인</th>\n",
       "      <th>외국인</th>\n",
       "      <th>고령자</th>\n",
       "      <th>외국인비율</th>\n",
       "      <th>고령자비율</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>중구</td>\n",
       "      <td>134593</td>\n",
       "      <td>125709</td>\n",
       "      <td>8884</td>\n",
       "      <td>21384</td>\n",
       "      <td>6.600640</td>\n",
       "      <td>15.887899</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>용산구</td>\n",
       "      <td>244444</td>\n",
       "      <td>229161</td>\n",
       "      <td>15283</td>\n",
       "      <td>36882</td>\n",
       "      <td>6.252148</td>\n",
       "      <td>15.088118</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>성동구</td>\n",
       "      <td>312711</td>\n",
       "      <td>304808</td>\n",
       "      <td>7903</td>\n",
       "      <td>41273</td>\n",
       "      <td>2.527254</td>\n",
       "      <td>13.198448</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>광진구</td>\n",
       "      <td>372298</td>\n",
       "      <td>357703</td>\n",
       "      <td>14595</td>\n",
       "      <td>43953</td>\n",
       "      <td>3.920247</td>\n",
       "      <td>11.805865</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>동대문구</td>\n",
       "      <td>366011</td>\n",
       "      <td>350647</td>\n",
       "      <td>15364</td>\n",
       "      <td>55718</td>\n",
       "      <td>4.197688</td>\n",
       "      <td>15.223040</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "     구별     인구수     한국인    외국인    고령자     외국인비율      고령자비율\n",
       "2    중구  134593  125709   8884  21384  6.600640  15.887899\n",
       "3   용산구  244444  229161  15283  36882  6.252148  15.088118\n",
       "4   성동구  312711  304808   7903  41273  2.527254  13.198448\n",
       "5   광진구  372298  357703  14595  43953  3.920247  11.805865\n",
       "6  동대문구  366011  350647  15364  55718  4.197688  15.223040"
      ]
     },
     "execution_count": 166,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# 외국인 비율, 고령자 비율\n",
    "\n",
    "pop_Seoul['외국인비율'] = pop_Seoul['외국인'] / pop_Seoul['인구수'] *100\n",
    "pop_Seoul['고령자비율'] = pop_Seoul['고령자'] / pop_Seoul['인구수'] *100\n",
    "pop_Seoul.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 136,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>자치구</th>\n",
       "      <th>계</th>\n",
       "      <th>계.1</th>\n",
       "      <th>계.2</th>\n",
       "      <th>65세이상고령자</th>\n",
       "      <th>외국인비율</th>\n",
       "      <th>고령자비율</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>10</th>\n",
       "      <td>도봉구</td>\n",
       "      <td>346234</td>\n",
       "      <td>344166</td>\n",
       "      <td>2068</td>\n",
       "      <td>53488</td>\n",
       "      <td>99.402716</td>\n",
       "      <td>0.597284</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>11</th>\n",
       "      <td>노원구</td>\n",
       "      <td>558075</td>\n",
       "      <td>554403</td>\n",
       "      <td>3672</td>\n",
       "      <td>74243</td>\n",
       "      <td>99.342024</td>\n",
       "      <td>0.657976</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>15</th>\n",
       "      <td>양천구</td>\n",
       "      <td>475018</td>\n",
       "      <td>471154</td>\n",
       "      <td>3864</td>\n",
       "      <td>55234</td>\n",
       "      <td>99.186557</td>\n",
       "      <td>0.813443</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>23</th>\n",
       "      <td>강남구</td>\n",
       "      <td>561052</td>\n",
       "      <td>556164</td>\n",
       "      <td>4888</td>\n",
       "      <td>65060</td>\n",
       "      <td>99.128780</td>\n",
       "      <td>0.871220</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>12</th>\n",
       "      <td>은평구</td>\n",
       "      <td>491202</td>\n",
       "      <td>486794</td>\n",
       "      <td>4408</td>\n",
       "      <td>74559</td>\n",
       "      <td>99.102610</td>\n",
       "      <td>0.897390</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "    자치구       계     계.1   계.2  65세이상고령자      외국인비율     고령자비율\n",
       "10  도봉구  346234  344166  2068     53488  99.402716  0.597284\n",
       "11  노원구  558075  554403  3672     74243  99.342024  0.657976\n",
       "15  양천구  475018  471154  3864     55234  99.186557  0.813443\n",
       "23  강남구  561052  556164  4888     65060  99.128780  0.871220\n",
       "12  은평구  491202  486794  4408     74559  99.102610  0.897390"
      ]
     },
     "execution_count": 136,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "pop_Seoul.sort_values(['외국인비율'], ascending=False).head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 163,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>구별</th>\n",
       "      <th>인구수</th>\n",
       "      <th>한국인</th>\n",
       "      <th>외국인</th>\n",
       "      <th>고령자</th>\n",
       "      <th>외국인비율</th>\n",
       "      <th>고령자비율</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>중구</td>\n",
       "      <td>134593</td>\n",
       "      <td>125709</td>\n",
       "      <td>8884</td>\n",
       "      <td>21384</td>\n",
       "      <td>93.399360</td>\n",
       "      <td>6.600640</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>용산구</td>\n",
       "      <td>244444</td>\n",
       "      <td>229161</td>\n",
       "      <td>15283</td>\n",
       "      <td>36882</td>\n",
       "      <td>93.747852</td>\n",
       "      <td>6.252148</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>성동구</td>\n",
       "      <td>312711</td>\n",
       "      <td>304808</td>\n",
       "      <td>7903</td>\n",
       "      <td>41273</td>\n",
       "      <td>97.472746</td>\n",
       "      <td>2.527254</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>광진구</td>\n",
       "      <td>372298</td>\n",
       "      <td>357703</td>\n",
       "      <td>14595</td>\n",
       "      <td>43953</td>\n",
       "      <td>96.079753</td>\n",
       "      <td>3.920247</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>동대문구</td>\n",
       "      <td>366011</td>\n",
       "      <td>350647</td>\n",
       "      <td>15364</td>\n",
       "      <td>55718</td>\n",
       "      <td>95.802312</td>\n",
       "      <td>4.197688</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "     구별     인구수     한국인    외국인    고령자      외국인비율     고령자비율\n",
       "2    중구  134593  125709   8884  21384  93.399360  6.600640\n",
       "3   용산구  244444  229161  15283  36882  93.747852  6.252148\n",
       "4   성동구  312711  304808   7903  41273  97.472746  2.527254\n",
       "5   광진구  372298  357703  14595  43953  96.079753  3.920247\n",
       "6  동대문구  366011  350647  15364  55718  95.802312  4.197688"
      ]
     },
     "execution_count": 163,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "pop_Seoul.rename(\n",
    "    columns={\n",
    "        pop_Seoul.columns[0]: '구별',\n",
    "        pop_Seoul.columns[1]: '인구수',\n",
    "        pop_Seoul.columns[2]: '한국인',\n",
    "        pop_Seoul.columns[3]: '외국인',\n",
    "        pop_Seoul.columns[4]: '고령자'\n",
    "    }, inplace=True \n",
    ")\n",
    "\n",
    "pop_Seoul.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 4.두 데이터 합치기"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "---"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### pandas에서 데이터 프레임을 병합하는 방법\n",
    "- pd.concat()\n",
    "- pd.merge()\n",
    "- pd.join()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 142,
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'left' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m~\\AppData\\Local\\Temp/ipykernel_4552/302817838.py\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[0mpd\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mmerge\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mleft\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mright\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m: name 'left' is not defined"
     ]
    }
   ],
   "source": [
    "pd.merge(left, right)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 154,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>key</th>\n",
       "      <th>A</th>\n",
       "      <th>B</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>K0</td>\n",
       "      <td>A0</td>\n",
       "      <td>B0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>K4</td>\n",
       "      <td>A1</td>\n",
       "      <td>B1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>K2</td>\n",
       "      <td>A2</td>\n",
       "      <td>B2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>K3</td>\n",
       "      <td>A3</td>\n",
       "      <td>B3</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "  key   A   B\n",
       "0  K0  A0  B0\n",
       "1  K4  A1  B1\n",
       "2  K2  A2  B2\n",
       "3  K3  A3  B3"
      ]
     },
     "execution_count": 154,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#딕셔너리 안에 리스트 형태\n",
    "\n",
    "left = pd.DataFrame({\n",
    "        'key' : ['K0', 'K4', 'K2', 'K3'],\n",
    "        'A' : ['A0', 'A1', 'A2', 'A3',],\n",
    "        'B' : ['B0', 'B1', 'B2', 'B3']\n",
    "    \n",
    "})\n",
    "left"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 149,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>key</th>\n",
       "      <th>C</th>\n",
       "      <th>D</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>K0</td>\n",
       "      <td>C0</td>\n",
       "      <td>D0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>K1</td>\n",
       "      <td>C1</td>\n",
       "      <td>D1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>K2</td>\n",
       "      <td>C2</td>\n",
       "      <td>D2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>K3</td>\n",
       "      <td>C3</td>\n",
       "      <td>D3</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "  key   C   D\n",
       "0  K0  C0  D0\n",
       "1  K1  C1  D1\n",
       "2  K2  C2  D2\n",
       "3  K3  C3  D3"
      ]
     },
     "execution_count": 149,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# 리스트 안의 딕셔너리 형태\n",
    "\n",
    "right = pd.DataFrame([\n",
    "    {'key':'K0', 'C' : 'C0', 'D':'D0' },\n",
    "    {'key':'K1', 'C' : 'C1', 'D':'D1' },\n",
    "    {'key':'K2', 'C' : 'C2', 'D':'D2' },\n",
    "    {'key':'K3', 'C' : 'C3', 'D':'D3' }\n",
    "])\n",
    "right"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### pd.merge()\n",
    "- 두 데이터 프레임에서 컬럼이나 인덱스를 기준으로 잡고 병합하는 방법\n",
    "- 기준이 되는 컬럼이나 인덱스를 키값이라고 합니다.\n",
    "- 기준이 되는 키값은 두 데이터 프레임에 모두 포함되어 있어야 합니다."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 156,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>key</th>\n",
       "      <th>A</th>\n",
       "      <th>B</th>\n",
       "      <th>C</th>\n",
       "      <th>D</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>K0</td>\n",
       "      <td>A0</td>\n",
       "      <td>B0</td>\n",
       "      <td>C0</td>\n",
       "      <td>D0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>K2</td>\n",
       "      <td>A2</td>\n",
       "      <td>B2</td>\n",
       "      <td>C2</td>\n",
       "      <td>D2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>K3</td>\n",
       "      <td>A3</td>\n",
       "      <td>B3</td>\n",
       "      <td>C3</td>\n",
       "      <td>D3</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "  key   A   B   C   D\n",
       "0  K0  A0  B0  C0  D0\n",
       "1  K2  A2  B2  C2  D2\n",
       "2  K3  A3  B3  C3  D3"
      ]
     },
     "execution_count": 156,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "pd.merge(left, right, on='key')\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 157,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>key</th>\n",
       "      <th>A</th>\n",
       "      <th>B</th>\n",
       "      <th>C</th>\n",
       "      <th>D</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>K0</td>\n",
       "      <td>A0</td>\n",
       "      <td>B0</td>\n",
       "      <td>C0</td>\n",
       "      <td>D0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>K4</td>\n",
       "      <td>A1</td>\n",
       "      <td>B1</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>K2</td>\n",
       "      <td>A2</td>\n",
       "      <td>B2</td>\n",
       "      <td>C2</td>\n",
       "      <td>D2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>K3</td>\n",
       "      <td>A3</td>\n",
       "      <td>B3</td>\n",
       "      <td>C3</td>\n",
       "      <td>D3</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "  key   A   B    C    D\n",
       "0  K0  A0  B0   C0   D0\n",
       "1  K4  A1  B1  NaN  NaN\n",
       "2  K2  A2  B2   C2   D2\n",
       "3  K3  A3  B3   C3   D3"
      ]
     },
     "execution_count": 157,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "pd.merge(left, right, how='left' ,on='key')\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 158,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>key</th>\n",
       "      <th>A</th>\n",
       "      <th>B</th>\n",
       "      <th>C</th>\n",
       "      <th>D</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>K0</td>\n",
       "      <td>A0</td>\n",
       "      <td>B0</td>\n",
       "      <td>C0</td>\n",
       "      <td>D0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>K1</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>C1</td>\n",
       "      <td>D1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>K2</td>\n",
       "      <td>A2</td>\n",
       "      <td>B2</td>\n",
       "      <td>C2</td>\n",
       "      <td>D2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>K3</td>\n",
       "      <td>A3</td>\n",
       "      <td>B3</td>\n",
       "      <td>C3</td>\n",
       "      <td>D3</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "  key    A    B   C   D\n",
       "0  K0   A0   B0  C0  D0\n",
       "1  K1  NaN  NaN  C1  D1\n",
       "2  K2   A2   B2  C2  D2\n",
       "3  K3   A3   B3  C3  D3"
      ]
     },
     "execution_count": 158,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "pd.merge(left, right, how='right' ,on='key')\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 159,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>key</th>\n",
       "      <th>A</th>\n",
       "      <th>B</th>\n",
       "      <th>C</th>\n",
       "      <th>D</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>K0</td>\n",
       "      <td>A0</td>\n",
       "      <td>B0</td>\n",
       "      <td>C0</td>\n",
       "      <td>D0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>K4</td>\n",
       "      <td>A1</td>\n",
       "      <td>B1</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>K2</td>\n",
       "      <td>A2</td>\n",
       "      <td>B2</td>\n",
       "      <td>C2</td>\n",
       "      <td>D2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>K3</td>\n",
       "      <td>A3</td>\n",
       "      <td>B3</td>\n",
       "      <td>C3</td>\n",
       "      <td>D3</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>K1</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>C1</td>\n",
       "      <td>D1</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "  key    A    B    C    D\n",
       "0  K0   A0   B0   C0   D0\n",
       "1  K4   A1   B1  NaN  NaN\n",
       "2  K2   A2   B2   C2   D2\n",
       "3  K3   A3   B3   C3   D3\n",
       "4  K1  NaN  NaN   C1   D1"
      ]
     },
     "execution_count": 159,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "pd.merge(left, right, how='outer' ,on='key')\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "---"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 160,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>구별</th>\n",
       "      <th>소계</th>\n",
       "      <th>2013년도 이전</th>\n",
       "      <th>2014년</th>\n",
       "      <th>2015년</th>\n",
       "      <th>2016년</th>\n",
       "      <th>최근증가율</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>강남구</td>\n",
       "      <td>3238</td>\n",
       "      <td>1292</td>\n",
       "      <td>430</td>\n",
       "      <td>584</td>\n",
       "      <td>932</td>\n",
       "      <td>150.619195</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "    구별    소계  2013년도 이전  2014년  2015년  2016년       최근증가율\n",
       "0  강남구  3238       1292    430    584    932  150.619195"
      ]
     },
     "execution_count": 160,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "CCTV_Seoul.head(1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 167,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>구별</th>\n",
       "      <th>인구수</th>\n",
       "      <th>한국인</th>\n",
       "      <th>외국인</th>\n",
       "      <th>고령자</th>\n",
       "      <th>외국인비율</th>\n",
       "      <th>고령자비율</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>중구</td>\n",
       "      <td>134593</td>\n",
       "      <td>125709</td>\n",
       "      <td>8884</td>\n",
       "      <td>21384</td>\n",
       "      <td>6.60064</td>\n",
       "      <td>15.887899</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   구별     인구수     한국인   외국인    고령자    외국인비율      고령자비율\n",
       "2  중구  134593  125709  8884  21384  6.60064  15.887899"
      ]
     },
     "execution_count": 167,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "pop_Seoul.head(1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 168,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>구별</th>\n",
       "      <th>소계</th>\n",
       "      <th>2013년도 이전</th>\n",
       "      <th>2014년</th>\n",
       "      <th>2015년</th>\n",
       "      <th>2016년</th>\n",
       "      <th>최근증가율</th>\n",
       "      <th>인구수</th>\n",
       "      <th>한국인</th>\n",
       "      <th>외국인</th>\n",
       "      <th>고령자</th>\n",
       "      <th>외국인비율</th>\n",
       "      <th>고령자비율</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>강남구</td>\n",
       "      <td>3238</td>\n",
       "      <td>1292</td>\n",
       "      <td>430</td>\n",
       "      <td>584</td>\n",
       "      <td>932</td>\n",
       "      <td>150.619195</td>\n",
       "      <td>561052</td>\n",
       "      <td>556164</td>\n",
       "      <td>4888</td>\n",
       "      <td>65060</td>\n",
       "      <td>0.871220</td>\n",
       "      <td>11.596073</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>강동구</td>\n",
       "      <td>1010</td>\n",
       "      <td>379</td>\n",
       "      <td>99</td>\n",
       "      <td>155</td>\n",
       "      <td>377</td>\n",
       "      <td>166.490765</td>\n",
       "      <td>440359</td>\n",
       "      <td>436223</td>\n",
       "      <td>4136</td>\n",
       "      <td>56161</td>\n",
       "      <td>0.939234</td>\n",
       "      <td>12.753458</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>강북구</td>\n",
       "      <td>831</td>\n",
       "      <td>369</td>\n",
       "      <td>120</td>\n",
       "      <td>138</td>\n",
       "      <td>204</td>\n",
       "      <td>125.203252</td>\n",
       "      <td>328002</td>\n",
       "      <td>324479</td>\n",
       "      <td>3523</td>\n",
       "      <td>56530</td>\n",
       "      <td>1.074079</td>\n",
       "      <td>17.234651</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>강서구</td>\n",
       "      <td>911</td>\n",
       "      <td>388</td>\n",
       "      <td>258</td>\n",
       "      <td>184</td>\n",
       "      <td>81</td>\n",
       "      <td>134.793814</td>\n",
       "      <td>608255</td>\n",
       "      <td>601691</td>\n",
       "      <td>6564</td>\n",
       "      <td>76032</td>\n",
       "      <td>1.079153</td>\n",
       "      <td>12.500021</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>관악구</td>\n",
       "      <td>2109</td>\n",
       "      <td>846</td>\n",
       "      <td>260</td>\n",
       "      <td>390</td>\n",
       "      <td>613</td>\n",
       "      <td>149.290780</td>\n",
       "      <td>520929</td>\n",
       "      <td>503297</td>\n",
       "      <td>17632</td>\n",
       "      <td>70046</td>\n",
       "      <td>3.384722</td>\n",
       "      <td>13.446362</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "    구별    소계  2013년도 이전  2014년  2015년  2016년       최근증가율     인구수     한국인  \\\n",
       "0  강남구  3238       1292    430    584    932  150.619195  561052  556164   \n",
       "1  강동구  1010        379     99    155    377  166.490765  440359  436223   \n",
       "2  강북구   831        369    120    138    204  125.203252  328002  324479   \n",
       "3  강서구   911        388    258    184     81  134.793814  608255  601691   \n",
       "4  관악구  2109        846    260    390    613  149.290780  520929  503297   \n",
       "\n",
       "     외국인    고령자     외국인비율      고령자비율  \n",
       "0   4888  65060  0.871220  11.596073  \n",
       "1   4136  56161  0.939234  12.753458  \n",
       "2   3523  56530  1.074079  17.234651  \n",
       "3   6564  76032  1.079153  12.500021  \n",
       "4  17632  70046  3.384722  13.446362  "
      ]
     },
     "execution_count": 168,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data_result = pd.merge(CCTV_Seoul, pop_Seoul, on='구별')\n",
    "data_result.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 년도별 데이터 컬럼 삭제\n",
    "- del\n",
    "- drop()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 169,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>구별</th>\n",
       "      <th>소계</th>\n",
       "      <th>2014년</th>\n",
       "      <th>2015년</th>\n",
       "      <th>2016년</th>\n",
       "      <th>최근증가율</th>\n",
       "      <th>인구수</th>\n",
       "      <th>한국인</th>\n",
       "      <th>외국인</th>\n",
       "      <th>고령자</th>\n",
       "      <th>외국인비율</th>\n",
       "      <th>고령자비율</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>강남구</td>\n",
       "      <td>3238</td>\n",
       "      <td>430</td>\n",
       "      <td>584</td>\n",
       "      <td>932</td>\n",
       "      <td>150.619195</td>\n",
       "      <td>561052</td>\n",
       "      <td>556164</td>\n",
       "      <td>4888</td>\n",
       "      <td>65060</td>\n",
       "      <td>0.871220</td>\n",
       "      <td>11.596073</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>강동구</td>\n",
       "      <td>1010</td>\n",
       "      <td>99</td>\n",
       "      <td>155</td>\n",
       "      <td>377</td>\n",
       "      <td>166.490765</td>\n",
       "      <td>440359</td>\n",
       "      <td>436223</td>\n",
       "      <td>4136</td>\n",
       "      <td>56161</td>\n",
       "      <td>0.939234</td>\n",
       "      <td>12.753458</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>강북구</td>\n",
       "      <td>831</td>\n",
       "      <td>120</td>\n",
       "      <td>138</td>\n",
       "      <td>204</td>\n",
       "      <td>125.203252</td>\n",
       "      <td>328002</td>\n",
       "      <td>324479</td>\n",
       "      <td>3523</td>\n",
       "      <td>56530</td>\n",
       "      <td>1.074079</td>\n",
       "      <td>17.234651</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>강서구</td>\n",
       "      <td>911</td>\n",
       "      <td>258</td>\n",
       "      <td>184</td>\n",
       "      <td>81</td>\n",
       "      <td>134.793814</td>\n",
       "      <td>608255</td>\n",
       "      <td>601691</td>\n",
       "      <td>6564</td>\n",
       "      <td>76032</td>\n",
       "      <td>1.079153</td>\n",
       "      <td>12.500021</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>관악구</td>\n",
       "      <td>2109</td>\n",
       "      <td>260</td>\n",
       "      <td>390</td>\n",
       "      <td>613</td>\n",
       "      <td>149.290780</td>\n",
       "      <td>520929</td>\n",
       "      <td>503297</td>\n",
       "      <td>17632</td>\n",
       "      <td>70046</td>\n",
       "      <td>3.384722</td>\n",
       "      <td>13.446362</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "    구별    소계  2014년  2015년  2016년       최근증가율     인구수     한국인    외국인    고령자  \\\n",
       "0  강남구  3238    430    584    932  150.619195  561052  556164   4888  65060   \n",
       "1  강동구  1010     99    155    377  166.490765  440359  436223   4136  56161   \n",
       "2  강북구   831    120    138    204  125.203252  328002  324479   3523  56530   \n",
       "3  강서구   911    258    184     81  134.793814  608255  601691   6564  76032   \n",
       "4  관악구  2109    260    390    613  149.290780  520929  503297  17632  70046   \n",
       "\n",
       "      외국인비율      고령자비율  \n",
       "0  0.871220  11.596073  \n",
       "1  0.939234  12.753458  \n",
       "2  1.074079  17.234651  \n",
       "3  1.079153  12.500021  \n",
       "4  3.384722  13.446362  "
      ]
     },
     "execution_count": 169,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "del data_result['2013년도 이전']\n",
    "data_result.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 170,
   "metadata": {},
   "outputs": [],
   "source": [
    "del data_result['2014년']\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 171,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>구별</th>\n",
       "      <th>소계</th>\n",
       "      <th>2015년</th>\n",
       "      <th>2016년</th>\n",
       "      <th>최근증가율</th>\n",
       "      <th>인구수</th>\n",
       "      <th>한국인</th>\n",
       "      <th>외국인</th>\n",
       "      <th>고령자</th>\n",
       "      <th>외국인비율</th>\n",
       "      <th>고령자비율</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>강남구</td>\n",
       "      <td>3238</td>\n",
       "      <td>584</td>\n",
       "      <td>932</td>\n",
       "      <td>150.619195</td>\n",
       "      <td>561052</td>\n",
       "      <td>556164</td>\n",
       "      <td>4888</td>\n",
       "      <td>65060</td>\n",
       "      <td>0.871220</td>\n",
       "      <td>11.596073</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>강동구</td>\n",
       "      <td>1010</td>\n",
       "      <td>155</td>\n",
       "      <td>377</td>\n",
       "      <td>166.490765</td>\n",
       "      <td>440359</td>\n",
       "      <td>436223</td>\n",
       "      <td>4136</td>\n",
       "      <td>56161</td>\n",
       "      <td>0.939234</td>\n",
       "      <td>12.753458</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>강북구</td>\n",
       "      <td>831</td>\n",
       "      <td>138</td>\n",
       "      <td>204</td>\n",
       "      <td>125.203252</td>\n",
       "      <td>328002</td>\n",
       "      <td>324479</td>\n",
       "      <td>3523</td>\n",
       "      <td>56530</td>\n",
       "      <td>1.074079</td>\n",
       "      <td>17.234651</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "    구별    소계  2015년  2016년       최근증가율     인구수     한국인   외국인    고령자     외국인비율  \\\n",
       "0  강남구  3238    584    932  150.619195  561052  556164  4888  65060  0.871220   \n",
       "1  강동구  1010    155    377  166.490765  440359  436223  4136  56161  0.939234   \n",
       "2  강북구   831    138    204  125.203252  328002  324479  3523  56530  1.074079   \n",
       "\n",
       "       고령자비율  \n",
       "0  11.596073  \n",
       "1  12.753458  \n",
       "2  17.234651  "
      ]
     },
     "execution_count": 171,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data_result.head(3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 172,
   "metadata": {},
   "outputs": [],
   "source": [
    "data_result.drop(['2015년', '2016년'], axis=1, inplace=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 173,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>구별</th>\n",
       "      <th>소계</th>\n",
       "      <th>최근증가율</th>\n",
       "      <th>인구수</th>\n",
       "      <th>한국인</th>\n",
       "      <th>외국인</th>\n",
       "      <th>고령자</th>\n",
       "      <th>외국인비율</th>\n",
       "      <th>고령자비율</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>강남구</td>\n",
       "      <td>3238</td>\n",
       "      <td>150.619195</td>\n",
       "      <td>561052</td>\n",
       "      <td>556164</td>\n",
       "      <td>4888</td>\n",
       "      <td>65060</td>\n",
       "      <td>0.871220</td>\n",
       "      <td>11.596073</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>강동구</td>\n",
       "      <td>1010</td>\n",
       "      <td>166.490765</td>\n",
       "      <td>440359</td>\n",
       "      <td>436223</td>\n",
       "      <td>4136</td>\n",
       "      <td>56161</td>\n",
       "      <td>0.939234</td>\n",
       "      <td>12.753458</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>강북구</td>\n",
       "      <td>831</td>\n",
       "      <td>125.203252</td>\n",
       "      <td>328002</td>\n",
       "      <td>324479</td>\n",
       "      <td>3523</td>\n",
       "      <td>56530</td>\n",
       "      <td>1.074079</td>\n",
       "      <td>17.234651</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>강서구</td>\n",
       "      <td>911</td>\n",
       "      <td>134.793814</td>\n",
       "      <td>608255</td>\n",
       "      <td>601691</td>\n",
       "      <td>6564</td>\n",
       "      <td>76032</td>\n",
       "      <td>1.079153</td>\n",
       "      <td>12.500021</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>관악구</td>\n",
       "      <td>2109</td>\n",
       "      <td>149.290780</td>\n",
       "      <td>520929</td>\n",
       "      <td>503297</td>\n",
       "      <td>17632</td>\n",
       "      <td>70046</td>\n",
       "      <td>3.384722</td>\n",
       "      <td>13.446362</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "    구별    소계       최근증가율     인구수     한국인    외국인    고령자     외국인비율      고령자비율\n",
       "0  강남구  3238  150.619195  561052  556164   4888  65060  0.871220  11.596073\n",
       "1  강동구  1010  166.490765  440359  436223   4136  56161  0.939234  12.753458\n",
       "2  강북구   831  125.203252  328002  324479   3523  56530  1.074079  17.234651\n",
       "3  강서구   911  134.793814  608255  601691   6564  76032  1.079153  12.500021\n",
       "4  관악구  2109  149.290780  520929  503297  17632  70046  3.384722  13.446362"
      ]
     },
     "execution_count": 173,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data_result.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 인덱스 변경\n",
    "- set_index()\n",
    "- 선택한 컬럼을 데이터 프레임의 인덱스로 지정"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 174,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>소계</th>\n",
       "      <th>최근증가율</th>\n",
       "      <th>인구수</th>\n",
       "      <th>한국인</th>\n",
       "      <th>외국인</th>\n",
       "      <th>고령자</th>\n",
       "      <th>외국인비율</th>\n",
       "      <th>고령자비율</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>구별</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>강남구</th>\n",
       "      <td>3238</td>\n",
       "      <td>150.619195</td>\n",
       "      <td>561052</td>\n",
       "      <td>556164</td>\n",
       "      <td>4888</td>\n",
       "      <td>65060</td>\n",
       "      <td>0.871220</td>\n",
       "      <td>11.596073</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>강동구</th>\n",
       "      <td>1010</td>\n",
       "      <td>166.490765</td>\n",
       "      <td>440359</td>\n",
       "      <td>436223</td>\n",
       "      <td>4136</td>\n",
       "      <td>56161</td>\n",
       "      <td>0.939234</td>\n",
       "      <td>12.753458</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>강북구</th>\n",
       "      <td>831</td>\n",
       "      <td>125.203252</td>\n",
       "      <td>328002</td>\n",
       "      <td>324479</td>\n",
       "      <td>3523</td>\n",
       "      <td>56530</td>\n",
       "      <td>1.074079</td>\n",
       "      <td>17.234651</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>강서구</th>\n",
       "      <td>911</td>\n",
       "      <td>134.793814</td>\n",
       "      <td>608255</td>\n",
       "      <td>601691</td>\n",
       "      <td>6564</td>\n",
       "      <td>76032</td>\n",
       "      <td>1.079153</td>\n",
       "      <td>12.500021</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>관악구</th>\n",
       "      <td>2109</td>\n",
       "      <td>149.290780</td>\n",
       "      <td>520929</td>\n",
       "      <td>503297</td>\n",
       "      <td>17632</td>\n",
       "      <td>70046</td>\n",
       "      <td>3.384722</td>\n",
       "      <td>13.446362</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "       소계       최근증가율     인구수     한국인    외국인    고령자     외국인비율      고령자비율\n",
       "구별                                                                      \n",
       "강남구  3238  150.619195  561052  556164   4888  65060  0.871220  11.596073\n",
       "강동구  1010  166.490765  440359  436223   4136  56161  0.939234  12.753458\n",
       "강북구   831  125.203252  328002  324479   3523  56530  1.074079  17.234651\n",
       "강서구   911  134.793814  608255  601691   6564  76032  1.079153  12.500021\n",
       "관악구  2109  149.290780  520929  503297  17632  70046  3.384722  13.446362"
      ]
     },
     "execution_count": 174,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data_result.set_index('구별', inplace=True)\n",
    "data_result.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 상관계수\n",
    "- corr()\n",
    "- correlation 의 약자입니다.\n",
    "- 상관계수가 0.2 이상인 데이터를 비교"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 175,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>소계</th>\n",
       "      <th>최근증가율</th>\n",
       "      <th>인구수</th>\n",
       "      <th>한국인</th>\n",
       "      <th>외국인</th>\n",
       "      <th>고령자</th>\n",
       "      <th>외국인비율</th>\n",
       "      <th>고령자비율</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>소계</th>\n",
       "      <td>1.000000</td>\n",
       "      <td>-0.311987</td>\n",
       "      <td>0.267334</td>\n",
       "      <td>0.261189</td>\n",
       "      <td>0.031542</td>\n",
       "      <td>0.194263</td>\n",
       "      <td>-0.055409</td>\n",
       "      <td>-0.289987</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>최근증가율</th>\n",
       "      <td>-0.311987</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.089811</td>\n",
       "      <td>0.099062</td>\n",
       "      <td>-0.159121</td>\n",
       "      <td>0.126772</td>\n",
       "      <td>-0.168722</td>\n",
       "      <td>0.075324</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>인구수</th>\n",
       "      <td>0.267334</td>\n",
       "      <td>0.089811</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.997859</td>\n",
       "      <td>-0.194693</td>\n",
       "      <td>0.925172</td>\n",
       "      <td>-0.571380</td>\n",
       "      <td>-0.596381</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>한국인</th>\n",
       "      <td>0.261189</td>\n",
       "      <td>0.099062</td>\n",
       "      <td>0.997859</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>-0.258419</td>\n",
       "      <td>0.924846</td>\n",
       "      <td>-0.620668</td>\n",
       "      <td>-0.586506</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>외국인</th>\n",
       "      <td>0.031542</td>\n",
       "      <td>-0.159121</td>\n",
       "      <td>-0.194693</td>\n",
       "      <td>-0.258419</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>-0.204951</td>\n",
       "      <td>0.868861</td>\n",
       "      <td>-0.012851</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>고령자</th>\n",
       "      <td>0.194263</td>\n",
       "      <td>0.126772</td>\n",
       "      <td>0.925172</td>\n",
       "      <td>0.924846</td>\n",
       "      <td>-0.204951</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>-0.593068</td>\n",
       "      <td>-0.267379</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>외국인비율</th>\n",
       "      <td>-0.055409</td>\n",
       "      <td>-0.168722</td>\n",
       "      <td>-0.571380</td>\n",
       "      <td>-0.620668</td>\n",
       "      <td>0.868861</td>\n",
       "      <td>-0.593068</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.190727</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>고령자비율</th>\n",
       "      <td>-0.289987</td>\n",
       "      <td>0.075324</td>\n",
       "      <td>-0.596381</td>\n",
       "      <td>-0.586506</td>\n",
       "      <td>-0.012851</td>\n",
       "      <td>-0.267379</td>\n",
       "      <td>0.190727</td>\n",
       "      <td>1.000000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "             소계     최근증가율       인구수       한국인       외국인       고령자     외국인비율  \\\n",
       "소계     1.000000 -0.311987  0.267334  0.261189  0.031542  0.194263 -0.055409   \n",
       "최근증가율 -0.311987  1.000000  0.089811  0.099062 -0.159121  0.126772 -0.168722   \n",
       "인구수    0.267334  0.089811  1.000000  0.997859 -0.194693  0.925172 -0.571380   \n",
       "한국인    0.261189  0.099062  0.997859  1.000000 -0.258419  0.924846 -0.620668   \n",
       "외국인    0.031542 -0.159121 -0.194693 -0.258419  1.000000 -0.204951  0.868861   \n",
       "고령자    0.194263  0.126772  0.925172  0.924846 -0.204951  1.000000 -0.593068   \n",
       "외국인비율 -0.055409 -0.168722 -0.571380 -0.620668  0.868861 -0.593068  1.000000   \n",
       "고령자비율 -0.289987  0.075324 -0.596381 -0.586506 -0.012851 -0.267379  0.190727   \n",
       "\n",
       "          고령자비율  \n",
       "소계    -0.289987  \n",
       "최근증가율  0.075324  \n",
       "인구수   -0.596381  \n",
       "한국인   -0.586506  \n",
       "외국인   -0.012851  \n",
       "고령자   -0.267379  \n",
       "외국인비율  0.190727  \n",
       "고령자비율  1.000000  "
      ]
     },
     "execution_count": 175,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data_result.corr()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 177,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "Index: 24 entries, 강남구 to 중랑구\n",
      "Data columns (total 8 columns):\n",
      " #   Column  Non-Null Count  Dtype  \n",
      "---  ------  --------------  -----  \n",
      " 0   소계      24 non-null     int64  \n",
      " 1   최근증가율   24 non-null     float64\n",
      " 2   인구수     24 non-null     int64  \n",
      " 3   한국인     24 non-null     int64  \n",
      " 4   외국인     24 non-null     int64  \n",
      " 5   고령자     24 non-null     int64  \n",
      " 6   외국인비율   24 non-null     float64\n",
      " 7   고령자비율   24 non-null     float64\n",
      "dtypes: float64(3), int64(5)\n",
      "memory usage: 1.7+ KB\n"
     ]
    }
   ],
   "source": [
    "data_result.info()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "corr() 는 문자열 같은게 들어가 있으면 연산이 되지 않는다."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 178,
   "metadata": {},
   "outputs": [],
   "source": [
    "data_result['CCTV비율'] = data_result['소계'] / data_result['인구수']\n",
    "data_result['CCTV비율'] = data_result['CCTV비율'] * 100"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 179,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>소계</th>\n",
       "      <th>최근증가율</th>\n",
       "      <th>인구수</th>\n",
       "      <th>한국인</th>\n",
       "      <th>외국인</th>\n",
       "      <th>고령자</th>\n",
       "      <th>외국인비율</th>\n",
       "      <th>고령자비율</th>\n",
       "      <th>CCTV비율</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>구별</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>강남구</th>\n",
       "      <td>3238</td>\n",
       "      <td>150.619195</td>\n",
       "      <td>561052</td>\n",
       "      <td>556164</td>\n",
       "      <td>4888</td>\n",
       "      <td>65060</td>\n",
       "      <td>0.871220</td>\n",
       "      <td>11.596073</td>\n",
       "      <td>0.577130</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>강동구</th>\n",
       "      <td>1010</td>\n",
       "      <td>166.490765</td>\n",
       "      <td>440359</td>\n",
       "      <td>436223</td>\n",
       "      <td>4136</td>\n",
       "      <td>56161</td>\n",
       "      <td>0.939234</td>\n",
       "      <td>12.753458</td>\n",
       "      <td>0.229358</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>강북구</th>\n",
       "      <td>831</td>\n",
       "      <td>125.203252</td>\n",
       "      <td>328002</td>\n",
       "      <td>324479</td>\n",
       "      <td>3523</td>\n",
       "      <td>56530</td>\n",
       "      <td>1.074079</td>\n",
       "      <td>17.234651</td>\n",
       "      <td>0.253352</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>강서구</th>\n",
       "      <td>911</td>\n",
       "      <td>134.793814</td>\n",
       "      <td>608255</td>\n",
       "      <td>601691</td>\n",
       "      <td>6564</td>\n",
       "      <td>76032</td>\n",
       "      <td>1.079153</td>\n",
       "      <td>12.500021</td>\n",
       "      <td>0.149773</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>관악구</th>\n",
       "      <td>2109</td>\n",
       "      <td>149.290780</td>\n",
       "      <td>520929</td>\n",
       "      <td>503297</td>\n",
       "      <td>17632</td>\n",
       "      <td>70046</td>\n",
       "      <td>3.384722</td>\n",
       "      <td>13.446362</td>\n",
       "      <td>0.404854</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "       소계       최근증가율     인구수     한국인    외국인    고령자     외국인비율      고령자비율  \\\n",
       "구별                                                                         \n",
       "강남구  3238  150.619195  561052  556164   4888  65060  0.871220  11.596073   \n",
       "강동구  1010  166.490765  440359  436223   4136  56161  0.939234  12.753458   \n",
       "강북구   831  125.203252  328002  324479   3523  56530  1.074079  17.234651   \n",
       "강서구   911  134.793814  608255  601691   6564  76032  1.079153  12.500021   \n",
       "관악구  2109  149.290780  520929  503297  17632  70046  3.384722  13.446362   \n",
       "\n",
       "       CCTV비율  \n",
       "구별             \n",
       "강남구  0.577130  \n",
       "강동구  0.229358  \n",
       "강북구  0.253352  \n",
       "강서구  0.149773  \n",
       "관악구  0.404854  "
      ]
     },
     "execution_count": 179,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data_result.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 180,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>소계</th>\n",
       "      <th>최근증가율</th>\n",
       "      <th>인구수</th>\n",
       "      <th>한국인</th>\n",
       "      <th>외국인</th>\n",
       "      <th>고령자</th>\n",
       "      <th>외국인비율</th>\n",
       "      <th>고령자비율</th>\n",
       "      <th>CCTV비율</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>구별</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>용산구</th>\n",
       "      <td>2096</td>\n",
       "      <td>53.216374</td>\n",
       "      <td>244444</td>\n",
       "      <td>229161</td>\n",
       "      <td>15283</td>\n",
       "      <td>36882</td>\n",
       "      <td>6.252148</td>\n",
       "      <td>15.088118</td>\n",
       "      <td>0.857456</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>중구</th>\n",
       "      <td>1023</td>\n",
       "      <td>147.699758</td>\n",
       "      <td>134593</td>\n",
       "      <td>125709</td>\n",
       "      <td>8884</td>\n",
       "      <td>21384</td>\n",
       "      <td>6.600640</td>\n",
       "      <td>15.887899</td>\n",
       "      <td>0.760069</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>강남구</th>\n",
       "      <td>3238</td>\n",
       "      <td>150.619195</td>\n",
       "      <td>561052</td>\n",
       "      <td>556164</td>\n",
       "      <td>4888</td>\n",
       "      <td>65060</td>\n",
       "      <td>0.871220</td>\n",
       "      <td>11.596073</td>\n",
       "      <td>0.577130</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>금천구</th>\n",
       "      <td>1348</td>\n",
       "      <td>100.000000</td>\n",
       "      <td>253491</td>\n",
       "      <td>235154</td>\n",
       "      <td>18337</td>\n",
       "      <td>34170</td>\n",
       "      <td>7.233787</td>\n",
       "      <td>13.479769</td>\n",
       "      <td>0.531774</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>양천구</th>\n",
       "      <td>2482</td>\n",
       "      <td>34.671731</td>\n",
       "      <td>475018</td>\n",
       "      <td>471154</td>\n",
       "      <td>3864</td>\n",
       "      <td>55234</td>\n",
       "      <td>0.813443</td>\n",
       "      <td>11.627770</td>\n",
       "      <td>0.522507</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "       소계       최근증가율     인구수     한국인    외국인    고령자     외국인비율      고령자비율  \\\n",
       "구별                                                                         \n",
       "용산구  2096   53.216374  244444  229161  15283  36882  6.252148  15.088118   \n",
       "중구   1023  147.699758  134593  125709   8884  21384  6.600640  15.887899   \n",
       "강남구  3238  150.619195  561052  556164   4888  65060  0.871220  11.596073   \n",
       "금천구  1348  100.000000  253491  235154  18337  34170  7.233787  13.479769   \n",
       "양천구  2482   34.671731  475018  471154   3864  55234  0.813443  11.627770   \n",
       "\n",
       "       CCTV비율  \n",
       "구별             \n",
       "용산구  0.857456  \n",
       "중구   0.760069  \n",
       "강남구  0.577130  \n",
       "금천구  0.531774  \n",
       "양천구  0.522507  "
      ]
     },
     "execution_count": 180,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data_result.sort_values(by='CCTV비율', ascending=False).head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "---"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# matplotib 기초"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 181,
   "metadata": {},
   "outputs": [],
   "source": [
    "import matplotlib.pyplot as plt\n",
    "from matplotlib import rc\n",
    "\n",
    "rc('font', family='Aerial Unicode MS') #Windows : Malgu Gothic\n",
    "# $matpoltlib inline\n",
    "get_ipython().run_line_magic('matplotlib', 'inline')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "import matplotlib.pyplot as plt  : matplotib에서 pyplot을 불러오는건데 matlab 의 시각화 툴이라고 생각하면 된다.  \n",
    "get_ipython().run_line_magic('matplotlib', 'inline') : 이 설정을 해줘야 밑에 그래프처럼 나타낼수가 있다."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### matplotlib 그래프 기본 형태\n",
    "- plt.figure(figsize=(10,6))  \n",
    "- plt.plot()  \n",
    "- plt.show  "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 182,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "findfont: Font family ['Aerial Unicode MS'] not found. Falling back to DejaVu Sans.\n"
     ]
    },
    {
     "data": {
      "image/png": "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",
      "text/plain": [
       "<Figure size 720x432 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.figure(figsize=(10,6))\n",
    "plt.plot([0,1,2,3,4,5,6,7,8,9], [1,1,2,3,4,2,3,5,-1,3])\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 예제1: 그래프 기초"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 삼각함수 그리기\n",
    "- np.arange(a,b,s): a부터 b까지 s의 간격\n",
    "- np.sin(value)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 186,
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "\n",
    "t = np.arange(0, 12, 0.01)\n",
    "y = np.sin(t)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 187,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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",
      "text/plain": [
       "<Figure size 720x432 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.figure(figsize=(10,6))\n",
    "plt.plot(t, np.sin(t))\n",
    "plt.plot(t, np.cos(t))\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "- 1. 격자무늬 추가\n",
    "- 2. 그래프 제목 추가\n",
    "- 3. x축, y축 제목 추가\n",
    "- 4. 주황색, 파란색 선 데이터 의미 구분"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 192,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAnAAAAGDCAYAAACr/S2JAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjUuMCwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy8/fFQqAAAACXBIWXMAAAsTAAALEwEAmpwYAACTuUlEQVR4nOzddXhUZ9r48e8zE3fihAQSIELw4qVAoGhLS922sruV7fq++6505V3vb92lvm1360pbXIO2FJdAjGAhxN1lnt8fZ0JTGiAhM/PMzHk+15UrJCPn5hBO7vPIfQspJZqmaZqmaZrnsKgOQNM0TdM0TesfncBpmqZpmqZ5GJ3AaZqmaZqmeRidwGmapmmapnkYncBpmqZpmqZ5GJ3AaZqmaZqmeRidwGmaZhpCiM8LIbY74X2FEOJ5IUSNEOLjfr62UQgx3NExaZrm3XxUB6BpmncQQpwE4oCuHt9+QUr5NTURudQ1wAIgUUrZ1J8XSilDnBOSpmneTCdwmqY50g1Syg2qg1BgGHCyv8mbpmnaldJTqJqmOZ0Q4gkhxFs9vv6tEGKjfepxkBBihRCiwj4FuUIIkdjjudlCiF8JIXbapxs/EEJECSFeFkLUCyF2CyGSezxfCiG+IYQoEkJUCiF+L4To9VonhMgQQqwXQlQLIfKEEHdc4u+QIIR43/7cQiHEw/bvPwg8C8ywx/fzXl47UgixRQhRZ4/p9QviHWn/8wtCiH8KIVYKIRqEELuEECMuF68QIkUIUdv99xRCPCuEKO/xupeEEN+y//kLQohj9vcvEkJ8qcfzjgkhlvb42sce71X2r6fb/x1qhRAHhRBZFztfmqY5l07gNE1zhf8FxtnXoM0CHgQekEYvPwvwPMYo1lCgBfjHBa+/C7gPGAKMAD60vyYSOAb89ILn3wxMBq4ClgFfvDAgIUQwsB54BYgF7gb+JYQYfZG/w6tAMZAA3Ab8PyHEtVLK54BHgQ+llCFSygtjAfglsA4YBCQCf7/IMbDH8XP7cwuBxy8Xr5TyBFAPTLS/xyygUQgxyv71bGCL/c/lwFIgDPgC8OfuBM3+d7y7RyyLgEop5T4hxBBgJfArjPP+HeBtIUTMJf4umqY5iU7gNE1zpOX20Znuj4cBpJTNwL3An4CXgK9LKYvtj1VJKd+WUjZLKRswEpY5F7zv81LK41LKOmA1cFxKuUFK2Qm8ySeJS7ffSimrpZSngb/w6aSk21KMac/npZSdUsp9wNsYydmnCCGSMNa5fV9K2SqlPIAx6nZfH89LB0aCmmB//aU2UrwjpfzY/nd7GZjQx3i3AHOEEPH2r9+yf52CkawdBJBSrrSfSyml3IKRWM6yv+YV4EYhRJD963vs3wPj32+VlHKVlNImpVwP7AGu6+M50DTNgXQCp2maI90kpYzo8fFM9wNSyo+BIkAAb3R/XwgRJIR4SghxSghRD2wFIoQQ1h7vW9bjzy29fH3hRoAzPf58CmPU7ELDgGk9E07gc0B8L89NAKrtCWbP9x3Sy3N78z2Mv/fHQogcIcRnRgR7KO3x52Y++btdLt4tQBbGaNtWIBsjEZ4DbJNS2gCEEEuEEB/Zp2FrMRKwaAApZSHGiOYN9iTuRj5J4IYBt19w/GuAwX08B5qmOZDexKBpmksIIb4K+AMlGAnNr+0P/S+QDkyTUpYKISYA+zESniuVBOTY/zzUfswLnQG2SCkX9OH9SoBIIURojyRuKHC2L8FIKUuB7jVz1wAbhBBb7QlTX10u3i3A7zGmebcA24EngVb71wgh/DFG7e4H3pNSdgghlvPpc909jWoBjvaI8QzwXynlw/2IWdM0J9EjcJqmOZ0QIg1j7dS9GNOO37MnagChGKNotUKISD67nu1KfFcYmyOSgG8Cr/fynBVAmhDiPiGEr/1jSo91Y+dJKc8AO4FfCyEChBDjMNbxvdyXYIQQt4tPNmbUAJJPl1vpi0vGK6UswDiP9wJbpZT1GCOVt/LJ+jc/jCS6AugUQiwBFl5wnNfs3/syn4y+gTH1fYMQYpEQwmo/D1k9/l6aprmQTuA0TXOkD+w7Mbs/3hVC+GD88v+tlPKgPdH4IfBf+4jQX4BAoBL4CFjjgDjeA/YCBzAW3j934RPsI2kLMTZIlGBMXf4WI8Hpzd1Asv257wI/ta8D64spwC4hRCPwPvBN+8aDPutjvFuAKvvav+6vBcaIZvd7fANjCrsGY43b+xcc5xzGJpGr6ZH42pPYZRj/dhUYI3LfRf8e0TQlhLEJTNM0zTsIISSQ2s/pSU3TNI+i75w0TdM0TdM8jE7gNE3TNE3TPIyeQtU0TdM0TfMwegRO0zRN0zTNw+gETtM0TdM0zcOYqpBvdHS0TE5OduoxmpqaCA4OduoxzEafU8fT59Sx9Pl0PH1OHUufT8dzxTndu3dvpZSy137DpkrgkpOT2bNnj1OPkZ2dTVZWllOPYTb6nDqePqeOpc+n4+lz6lj6fDqeK86pEOLUxR7TU6iapmmapmkeRidwmqZpmqZpHkYncJqmaZqmaR5GJ3CapmmapmkeRidwmqZpmqZpHkYncJqmaZqmaR5GJ3CapmmapmkeRidwmqZpmqZpHkYncJqmaZqmaR5GaQInhPi3EKJcCHHkIo8LIcTfhBCFQohDQoirejy2WAiRZ3/sMddFrWmapmmappbqEbgXgMWXeHwJkGr/eAR4AkAIYQX+aX88E7hbCJHp1Eg1TdM0TdPchNJeqFLKrUKI5Es8ZRnwHymlBD4SQkQIIQYDyUChlLIIQAjxmv25R50c8qXVnGRQ9T44GwoRyRAcpTQcFWqa2jlb20JNczt+Vgsxof4MiwrGahGqQ9M0tTrboboImipA2iAgDKJGgn+o6shcrry+lZK6VhpaOwjysxIbGkDioECE0NcJTesrd29mPwQ40+PrYvv3evv+tN7eQAjxCMboHXFxcWRnZzslUIDEM+8x/vi/4ZDxdUtAHNWRkyiLy6I+LA289OJ0psHGtuIODld2ca5JfuZxXwtkRFqZFGdl+mAfAnz6dx4aGxud+u9mRvqcOtbFzqdPRz2x5duILd9BaEMBVlv7px6XCJqDEqmMnkZZ3FyagxNdFLFrSSnJrbaxs6STnKouqls/e50I8oHMKCtTB/twVayV1uYm/TPqQPr/vOOpPqfunsD19pteXuL7n/2mlE8DTwNMnjxZZmVlOSy4z2gczb6NaVyVkQyVBQSe2cWQwg0MKVkFQ2dA1g9g+BznHd/FDpyp5Q9r89heWImf1cLVI6O5PyWKlOhgBgX50tElOVfXQk5JPZvzynkhp5l3iyQPXJ3Mo3OGE+TXtx+/7OxsnPrvZkL6nDrWZ85nczXs+At8/Ax0NENsJmQ+AoPHQ0gsWHygpQZRfozgk9sJPvkOw06/BRlLYe6PIM47VoRIKdl4rJw/rc/n6Ll6gv2sZKXHM2nYIIZFBREa4EtLRxfFNc0cLq5jw7Fy9hxoY0hEINcm+POTJbPxsape6eMd9P95x1N9Tt09gSsGknp8nQiUAH4X+b5aITHUh4+C9CxIX2J8r7UeDr5mXMz/cyOMvQMW/8ajp1cb2zr59apjvLzrNJHBfvzwugxun5TEoGC/Xp9/O/BTmcm+07U8vfU4f9tYwFt7zvCrm8cwLyPOtcFrmjNJCUfehtXfh+YqGHsbXP0NGDyu9+ePugHmfA8ay2H3s7DrSXhqFsz4KmT9EHwDXBu/A52ra+H/lh9hw7FykqOC+N1t47hhXAKBftbeXzANumySLfnl/Gvzcf5ztIY9/9jBb28dx9jEcNcGr2kewN1vbd4H7rfvRp0O1EkpzwG7gVQhRIoQwg+4y/5c9xMQBtMega/vg9nfg5x34clr4PQu1ZFdkfyyBq7/2zZe+fg0D16TwtbvzeWR2SMumrx1E0IwadggnrpvMm8+OoOwQF+++MIefvZ+Du2dNhdFr2lO1NEK730N3n4QBg2DR7fBrc9ePHnrKSQW5v4Qvr4fxt8FO/4Kzy2AquPOj9sJthVUsOSv29heWMmPrx/Fhm/P4Y7JSRdP3uysFsG8jDjefHQGX5ngT1VTG7c8sYMXdpzAWAqtaVo31WVEXgU+BNKFEMVCiAeFEI8KIR61P2UVUAQUAs8AXwGQUnYCXwPWAseAN6SUOS7/C/SHbwDM+xE8vBF8/OGF64yROQ+y/mgZN/9zB83tXbzxpRn839JMQvz7P4g7JTmS5V+dyeevTuaFnSf5/PMfU9fS4YSINc01/Nqq4PnFcOAl40btwfUQP7b/bxQcBcv+CXe/DrWn4Zm5cOpDxwfsRM9sLeKBf39MXGgAq785m4dmDe/3NKgQgqnxPqz91mxmp8bwsw+O8tjbh+ns0jd7mtZN9S7Uuy/zuAS+epHHVmEkeJ5l8Hh4JBveuA/e/ZIxzTKj17+iW3l7bzHfeesg44aE89R9k4kPH9jUToCvlZ/dOJqxQ8J57J1D3PHkh7z88DSiQ/wdFLGmuUjtaSbu/yHYGuGuVyDj+oG/Z/pi+NJWeOlW+O9NcNvzkHHdwN/XiaSU/GFdHv/cfJzrxsbz+9vGE3wFN3g9RQT58ewDk/nT+nz+vqmQqqZ2/nHPRAJ8Lz2Sp2lm4O5TqN4pMAI+95ax/mXtD2H7X1RHdElv7DnDd946yMwR0bz2yIwBJ2893TopkRe+MJVT1U3c++wuqpvaL/8iTXMX1Sfg+evw6WyA+5Y7JnnrNmgYfHEtxI2G1++FvNWOe28Hk1Ly+Mpj/HPzce6emsQ/7r5qwMlbNyEE/7swnV8uG83G3DK+9N+9etmFpqETOHV8/OH2F2H0LbDhp7DvP6oj6tXqw+f4/tuHuGZkNM8+MPmya1iuxMyR0Tz3wBROVBpJXEOrnk7VPEBTJbx0C7Q3cnD8ryBpiuOPERwF979njNy/8QCc2Ob4YzjAv7KP8+z2EzwwYxj/7+axWJxQ9/G+Gcn85paxbMmv4H/eOECXTa+J08xNJ3AqWaxw81MwYh588E23u8Ped7qGb71+gIlJETxz/2SnTlvMHBnNU/dNIq+sga+/ul+vddHcW3szvHIn1JfAPW/QGDrcecfyD4V734bIFHj1bihTW6/8Qm/vLeb3a/O4aUICP71htFOL8d45ZSg/vC6DlYfO8csV7nUeNM3VdAKnmo8f3PkSxI+Dtx+GinzVEQFQXNPMwy/uIS4swOnJW7es9Fh+sWw02XkV/GrlMacfT9OuiJTw3lfg7F649TlImur8YwZFwr3vgF8QvHYPtNQ4/5h9sPdUNd9/+xBXj4jid7eNd8rI24UemT2CB69J4YWdJ3ljz5nLv0DTvJRO4NyBXzDc9bIxrfraPUbtOIXaO2189eV9tHfaeP4LU4hy4caCz00bdv7i/M6+YpcdV9P6bNeTRjmg+T+FUUtdd9zwIXDHf6GuGN76Iti6XHfsXlQ2tvGVl/eREBHIE/dOws/Hdb9OfrAkg1mp0fz43SPsO+0eyaymuZpO4NxFeCLc/oLRK/H9rxt3+Yr8v1XHOFhcx+9vH8eImBCXH/8HSzKYmhzJj5cf4XhFo8uPr2kXdXoXrPux0TFh5rdcf/yh0+D6P8LxTbDtT64/vl2XTfKNV/dT29zBE/deRXigr0uP72O18Pe7JxIfHsDXX9mvyxBppqQTOHeSMsuoFXd0ORx8VUkI63JKeWHnSb44M4XFYwYricHHauFvd0/E38dijAR26cXKmhtoa4C3HzJutpb9U11v40kPwNjbIfvXcGa3khCe2nqcncer+OWyMYxOUNMlISLIj7/fPZGy+lZ+9O5hXehXMx2dwLmbmd+CYTNh1XeN0TgXqm5q54fvHmZ0QhiPLclw6bEvFB8ewJ/umEBuaQPvFuq7a80NrP0h1BfDzU8bpYBUuv6PEDYE3nnISCxdKLe0nj+vz+e6sfHcPjnRpce+0PikCP5nQRorDp3j7X1nlcaiaa6mEzh3070zVVhh+VfB5rrdmD99P4e6lg7+cPt4l65nuZi5GbHcPXUoa0506HUumlr564xSP1d/w5jGVC0gHG552ujWsOFnLjtse6eNb79+kPBAX365bIxTd5z21aNzRjAtJZKfv59DWX2r6nA0zWXU/5bWPisiCRb9Ck7vhP2uqQ+35sg5PjhYwtfnpTJqcJhLjtkXP7wug0EBgu++eZDWDrWLtjWTaqkx1qXGjDL6lbqLYTNg6pdg93Mu6638j82FHD1Xz+M3j3Xp5qZLsVoEv711HO1dNn72vnt3VNQ0R9IJnLuaeB8MuwbW/wQaypx6qPrWDn68PIfRCWF8OWuEU4/VX6EBvnxxjB/HK5r4V7ZnNvbWPNymX0FTOdz8hLFT3J3M+7GxJu+Db0Knc7uYHK9o5InsQm6akMCi0fFOPVZ/JUcH8835qaw+Usq6nFLV4WiaS+gEzl0JATf8BTpaYO0PnHqov6wvoKqpjd/cMg7ffjaddoUx0T7cOD6BJ7cc53RVs+pwNDMp2W+McE15GBImqo7ms/xDjPVwFcdgx1+ddhgpJT97P4cAXys/uj7TaccZiIdnDScjPpSfvJeju7lopuB+v621T0SnwqzvwJG34fhmpxwit7SeFz88yd1ThzI2Uc1usr744XWj8LUIfrFCT5FoLmKzwcrvQHC0e02dXihtEYy+Gbb+3lgT5wSrj5SyraCS7yxMJybUzUYh7XytFn5z6zjKGlr5x6ZC1eFomtPpBM7dzfwmRAyDtT9yeOFOKSU/fS+H0AAfvrsw3aHv7Wjx4QF849pUNhwrZ1Ouc6eUNQ2A/f+Fs3tgwS/V7zq9nIW/AmFxyoaGprZOfrniKJmDw/jctKEOf39HmpAUwW1XJfLvHSc4WdmkOhxNcyqdwLk73wBY8HMozzF+oTjQikPn2HWimu8uSmdQsJ9D39sZvjAzhRExwfzig6O0d+peqZoTtTXAxl9A0nQYf5fqaC4vPBFmfsMYrXfwhoanthZxrq6VX940Gh83XGJxoe8uSsfXauHXq3U7Ps27uf//Rg0ybzJ+kWz6lcPabLV32vj92jwy4kO5a4p731V38/Ox8OPrMzlZ1cxru50zVaRpAOz8OzRXwqLH1RXs7a+Z34TQwcaaWQeVHypvaOXZbUVcP3Ywk4ZFOuQ9nS02LICvZI1gbU4ZO49Xqg5H05xGJ3CeQAhY9P+gqQK2/9khb/na7tOcrm7m+4szsLqgAbWjZKXHMC0lkr9tLKCprVN1OJo3aiiDnf+AzGWQOFl1NH3nFwzX/gTO7jVG4hzgbxsLaO+08d1F7r3E4kIPzRrOkIhAHl95DJtNd2jQvJNO4DxF4iQYcxt89MSAy4o0tXXyt40FTEuJJCs9xkEBuoYQgseWZFDZ2M6z206oDkfzRlt+A11tcO1PVUfSf+PugrixkP3/oGtgOzGLKhp59eMz3DNtKMnRwQ4K0DUCfK18Z1EaOSX1rNFlRTRHkxL2voi1s0VpGDqB8yRzfwhd7QMehXtu+wkqG9t5bEmGW1RS76+JQwexeHQ8T289TmVjm+pwNG9SdRz2vgiTPg9R7lUTsU8sFqOfcnXRgPsp/2FdHgE+Fr5xbaqDgnOtG8cPYWRsCH9an0+XHoXTHClvNXzwDWIqdigNQydwniRqBIy/G/b8G+qurO9fbXM7T28tYvHoeCYOHeTgAF3nu4vTae208YQu7qs50tbfg9UP5nxfdSRXLm0xDJkEW34HnVd2g3PsXD2rDpfy4KzhRLtJx4X+sloE316QRmF5I+8f1H1SNQeRErJ/DZHDKYubqzQUncB5mjnfA2mDbX+4opf/e8dJGts6+dYCz7yr7jYiJoRlExJ4edcpPQqnOUbVcTj0Bkx5EEJiVUdz5YQwOjTUnTH6t16Bf2wqJNTfhwdnpjg4ONdaPDqezMFh/GVDAR1deue65gD5a6H0EMz6DtJiVRqKTuA8zaBhcNV9sO+/UHOqXy+tb+3ghR0nWDQ6jox49+l3eqW+Onck7Z02ntlWpDoUzRts/xNYfeHqr6uOZOCGz4VhM2HrH6Cjfw3e88saWHXkHJ+fmUx4kK+TAnQNi0XwvwvTOFXVzDv7ilWHo3k6KWHLbyFiKIy7Q3U0OoHzSLO+Y3ze+fd+vey/H56ivrWTr8/z7NG3biNiQlg6LoH/fniK6ibn9oHUvFzNSTj4mrH2LdS9+nxeESGMaeDGUjj4Sr9e+o9NhQT5Wvmih4++dZuXEcvYIeE8uaVIr4XTBub4RijZB7P+17jZU0wncJ4ofAiMv9Mo7NtY0aeXNLV18uy2IuZlxDJmiPu2zOqvr80bSUtHF//ernekagOw7U9GJ4OZ31QdieOkzDbWwu34K3T1reROYXkjHxwq4b4ZyR5R3LsvhBB8OWsEJyqbWHNE70jVrpCUxrrSsEQYf4/qaACdwHmuq79pLFDe9WSfnv7yrlPUNHfwtXkjnRyYa6XFhXLdmMG8sPMk9bqBtXYlas/AgVfgqvshLEF1NI4jBFzzP8bo4tHlfXrJvzYXEuBj5aFZ3jH61m3R6HiGRwfzxJZCpNSjcNoVOLEVzuyCa74FPu5xc6MTOE8VkwajlsLuZy7bnaG1o4unt57gmpHRXOXBO08v5stZI2hs6+S1j3V3Bu0K7HrS2BjkTaNv3dKvh+g02P4XYwThEkpqW3jvYAl3Tx3qsTtPL8ZqEXxpznCOnK1nW4HuzqBdge1/hpA4mHif6kjO0wmcJ5v5P9BaB3tfuOTT3j9YQmVjG1/O8sC6Vn0wZkg4M4ZH8fyOk3qnmdY/rXVG3bfRNxsLk72NxQIzvwVlh6FwwyWf+sLOkwB88Zpkp4elwk0ThxAX5s+/sgtVh6J5mrIcKNoM075k9Cd3EzqB82SJk4x1Lh/+86L1nqSUPLftBBnxoVw9IsrFAbrOI7OHc66ulZWHzqkORfMk+/4D7Q1w9ddUR+I8Y2831u1s+9NFn9LQ2sGru06zZEw8iYOCXBic6/j7WHl41nA+Kqpm3+ka1eFonuTDf4JvEEz6gupIPkVpAieEWCyEyBNCFAohHuvl8e8KIQ7YP44IIbqEEJH2x04KIQ7bH9vj+ujdxMxvGTvNDr/Z68PbCyvJK2vgoVnDPbLrQl/NSYshNTaEp7cW6TUuWt90dcBHT8KwayBhouponMfHD2Z8BU7vhJL9vT7l9d1naGjr5OFZw10cnGvdPXUooQE+etOT1ncNpUZ9yAmfg6BI1dF8irIETghhBf4JLAEygbuFEJk9nyOl/L2UcoKUcgLwA2CLlLK6x1Pm2h/3oI7TDjZiHsRkwK6nel3j8uy2E0SH+HPD+MEKgnMdi0Xw0KwUjp6r58PjVarD0TzB0fegvti7R9+6TbwX/EKM68QFOrtsPL/jJFOTIxmfFOH62Fwo2N+Hu6YksfpIKefq1Pax1DzEx8+ArROmf1l1JJ+hcgRuKlAopSySUrYDrwHLLvH8u4GBNffzRkIY8/Klh+D0R596qKCsgS35FTwwYxj+PmorRrvCsglDiA7x56mturCvdhlSws6/QVQqpC5SHY3zBYTDhHvgyNvQWP6ph1YfKeVsbYvX7Ty9mPtnJCOl5KWP+lcIXTOh9ibY8xxkXO+WvZFVJnBDgDM9vi62f+8zhBBBwGLg7R7flsA6IcReIcQjTovSE4y707hAX1BS5N87TuDvY+Fz04cpCsy1Anyt3D9jGFvyKyiqaFQdjubOTn8I5w4aU4sWkywFnvol6Go3ein38Nz2EyRHBXHtqDhFgblWUmQQ80fF8cqu07R2dKkOR3NnB1+FlhqY4Z6j9D4Kj93bgqyLLV66AdhxwfTpTClliRAiFlgvhMiVUm79zEGM5O4RgLi4OLKzswcY9qU1NjY6/Ri9GR4zj6Sj7/HRmjdpC4ihsV3y1p5mZib4cGj3TpfH40j9OafDOiVWAb95awf3jPKuUgiOpOrn1F2MOvoHoqzB7Kwbgs0B58FTzufYyEmE7niCD22TkBZfTtZ1ceBMK5/L8GPb1i2qw/sUZ57TicFdrGvu4Hevb2J2ovqK+q7gKT+jbkNKpuz+K7aQEewtaoUT2Z95iupzqjKBKwaSenydCJRc5Ll3ccH0qZSyxP65XAjxLsaU7GcSOCnl08DTAJMnT5ZZWVkDDvxSsrOzcfYxejU+Bf72HjN8jkLWT3l2WxEdtmN8/9YZjBrs2X1P+3tON1bvZ3NeOX958BqC/FT+iLsvZT+n7qCxHLZ+BFMeYva1jpk+9ZjzmdgJL93KnKhqGH8nj719iEDfEr53Zxbhge6VyDjznM6RkvfObGNnJfzf52Z59Qavbh7zM+ouTu6ALafhxn+QddXcXp+i+pyqnDvYDaQKIVKEEH4YSdr7Fz5JCBEOzAHe6/G9YCFEaPefgYXAEZdE7a4GDYP062DvC8j2Zl7edZpJwwZ5fPJ2Je6bMYyG1k7eP3Cx+wHN1Pb9B2wdMOVB1ZG43vB5xrq/XU9S19LB8gNnWTYhwe2SN2cTQvCFmcnkljaw60T15V+gmc/uZ42lSWNuVR3JRSlL4KSUncDXgLXAMeANKWWOEOJRIcSjPZ56M7BOStnU43txwHYhxEHgY2CllHKNq2J3W9O+BC3VFGz+Lycqm7h3uhcWJu2DycMGkREfyn8+PKVLimifZuuCPc9DyhyITlUdjetZLDD1YSjZR/bmdbR22LjXJGtkL7RswhDCA315eZfu4KJdoKEMjr0PE+4FP/eti6h09a6UcpWUMk1KOUJK+bj9e09KKZ/s8ZwXpJR3XfC6IinlePvH6O7Xml7yLIgaiXX/iwwK8mXJGO8uHXIxQgjun5HM0XP1umCn9mn5a43SIVMeUh2JOuPuRPoEYtn/IhOSIhgzJFx1REoE+Fq55aohrDlyjqrG3guhaya17z9G6ZDJX1QdySWZZPuVSQhBw+h7GdGaw1cy2wnw9f7SIRezbEICof4+/OdDXSpA62HPcxA62FhuYFaBEVQMvY657Vv4wuRo1dEodc/UoXR0Sd7eV6w6FM1ddHUa7SmHZ0H0SNXRXJJO4LzMK23X0CZ9uNOyUXUoSgX7+3DrpERWHy6lpqlddTiaO6guMvqBTvo8WM29ueWF9rmEiFauY7vqUJRKjQtlSvIgXv34jF5uoRkKPGeUXidwXqSzy8bz++vZGzyLsPy3ob1ZdUhK3TklifYuG+/uP6s6FM0d7H0BhBWuekB1JEqV1bfyVFEkZYEj8T3woupwlLtn2lBOVDbpDi6aYe+LEBIPaUtUR3JZOoHzIpvzKiitb8Vn6hehtQ6OLlcdklKjBocxPjGcN/bou2vT6+qAA69C2mIIM+fa0G5v7yumywbWKV8wihmf3ac6JKWWjBlsbGb4WG9mML36c1C43uha4gGj9DqB8yJv7DlDdIg/V11zPUSNNEYcTO6OKUnkljZwqLhOdSiaSgXroakcrrpPdSRKSSl5c08xU5Mjib76PvANgr3Pqw5LqQBfK7delci6nFIq9WYGczv4Ckib0TvYA+gEzktUNraxObecW64ago+P1Vjnc2YXlB9THZpSN4xPIMDXwut7zlz+yZr32v8ShMTByAWqI1Fq76kaTlQ2cfvkRHuNq1vg8NvQZu7Wc/dMS6KjS7JcL7cwLymN68SwmW7Z97Q3OoHzEsv3n6XTJrl9UqLxjXF3gcUHDryiNjDFwgJ8uW7sYD44UEJLu+57aEoNZZC/xugZ7AHTIs70xp4zBPtZuW6sfRp5wr3Q0QTHPlAbmGIjY0OZkBTBm3uK9XILszq109joNNFzRul1AucFpJS8secME5IiSI0LNb4ZEgOpi+DQ68a2aBO7c3ISDW2drDp8TnUomgqHXgfZ5THTIs7S1NbJikPnWDougWB/eyI7dDoMSoEDL6sNzg3cNimRvLIGckrqVYeiqbD/JfALhcwbVUfSZzqB8wKHiuvIL2s0pkV6mnA3NJbB8U1qAnMTU1MiSYkO1tOoZiSlkZwkToWYdNXRKLXy8Dma27s+fZ0QwliwfXIb1Ji7ZuIN4xLw87Hw1l5dE850WuuNTX9jbwW/YNXR9JlO4LzAm3vP4O9j4YbxCZ9+IHURBEYaCzNNTAjB7ZMT+fhENScqmy7/As17nN0LFbmmH30DeGtPMcOjg5k0bNCnHxhvb3Rz6HXXB+VGwoN8WZgZx/IDZ2nr1MstTCXnHeho9qjpU9AJnMdr7eji/QMlLB4TT1jABQ2pffxg3B2QuxJazN1S6rarErEIeEdXXDeX/f81dlqOvll1JEoVVTTy8clqbp+chBDi0w9GDIWU2cZIpcnXf902KZHa5g4255arDkVzpf0vQcwoGDJJdST9ohM4D7fuaBn1rZ3cPimp9yeMvxu62uHIO64NzM3EhgUwc2Q07+4/qxcpm0VHi/Fzn7kMAsJUR6PU2/uKsQi45aohvT9hwueg5iSc/tClcbmbWakxxIX562lUM6k6DsW7jSVHF97cuDmdwHm4t/cWkxAewNUjonp/wuDxEDva9LtRwfjlVVzTwp5T5h6NNI281dBW/8kUoUnZbJLl+0vsyUlA708adQP4hZh+M4PVIrh5YiKb8yqoaNA14Uzh8JuAgLG3q46k33QC58EqGtrYXljJsolDsFgucucghHFncXYPVOS7NkA3szAznkBfK+/s07WeTOHwm0bj+uRZqiNRau/pGs7WtnDTxISLP8kvGEbfBDnLod3c60RvmzSELpvkvQP6OuH1pDTWfqbMgrBL/P9wUzqB82ArD5XQZZPcNOEi0yLdxt5h9IA0+WaGYH8fFo+JZ+WhEr1I2ds1VxvdF8bcChar6miUWr7/LIG+VhZmxl/6iePvgfZGY82siY2MDWV8UgRv6xs973d2r1H7bdydqiO5IjqB82DLD5SQER9KenzopZ8YGgcj5hoV102+/uumiUOob+3Ui5S93dHlYOswNvGYWHunjZWHz7EgM+6T2m8XM3QGhCXC4bdcE5wbWzY+gWPn6iksb1AdiuZMh14HnwBjCYEH0gmchzpZ2cSBM7XcNPEyo2/dxt4OdafhzMfODczNzRwRRUyov55G9XaH3oDodIgfpzoSpbbkV1Db3MHNfblOWCxGHazjG6GpyvnBubGl4wZjEfD+gRLVoWjO0tVhbHJKX2K0lfNAOoHzUO8fLEEIuPHC2m8Xk3G9cadx+E3nBubmfKwWbhyfwOa8cmqb21WHozlD7WljN+W4OzxuV5mjLT9wlshgP65Jje7bC8bcBrZOYwTTxGLDArh6RDTvHSzRu9a91fHN0FxpLDHyUDqB80BSSpYfOMvU5EgSIgL79iL/UEhbDDnvmr611s0Th9DRJVlxSLfW8krdNykeuKvMkRpaO9hwtIyl4wbja+3jpT5+rDFyeeRt5wbnAW6ckMCpqmYOFtepDkVzhkOvQ+AgGDlfdSRXTCdwHujI2XqKKpr6Pn3abextxh3HiWynxOUpRieEkRoboneZeSMpjenTpOkwaJjqaJRac6SUtk4byy63yaknYS+ncGoH1Jm7Ftqi0fH4WS36OuGN2hqMzTqjbzEK3nsoncB5oOUHzuJrFSwZc5ldZRcauQD8w43NDCYmhOCG8QnsPlnDuboW1eFojlR62GidNc7co28A7x0oYWhkEFcNjejfC8fcYnw2+ShceKAvczNiWHHoHF02PY3qVXJXQmeLx+4+7aYTOA/TZZN8cLCErPRYIoL6eefga99tc+wDo0q9iS0dNxiAlXoa1bscfgMsPsadtYmV17ey83glN01I+GzrrMuJGmG0FNK7UVk2YQgVDW18VGTuTR1e5/CbEDEMkqaqjmRAdALnYT4qqqK8oe3ytd8uZuxt0N4ABescG5iHGR4TwuiEML0OzpvYbHDkXWNNS1Ck6miUWnHoHDYJN17xdeJ2KD0EFXmODczDzMuIJcTfR0+jepPmaijKNkaaPXyTk07gPMwHB0sI9rNy7ajYK3uDlNkQHGv63agAS8clcOBMLWeqm1WHojnC2T1QX2z60TeAlYfPkREfysjYkCt7g9E3g7CYfhQuwNfKwtFxrD5SSmuHLv7tFXJXGDutR9+sOpIB0wmcB+nosrE2p5T5mXEE+F5hdXmL1bjzyF8HrebeXXV+GvWwHoXzCjnvgtUP0herjkSpc3Ut7D1Vc/7n+4qExhstyA6/afri38smDKGhtZPsvArVoWiOkPMuRA73ihqROoHzIB8er6KmuYPrxg7gwgxGraeuNtO3zEmKDGJ8UgQfHNTFOj2ezWb08Rw532OLcjrKqsOlAAO/Toy9DWpOwLkDAw/Kg80cEUVksJ++0fMGTVVQtMU+wuzZ06egEziPsurwOYL9rMxJixnYGyVOhvAkOPqeYwLzYDeMG0xOST0nKs3dwNvjFe+GhhKvmBYZqFWHzzFqcBjDY65w+rRbxlKjh7LJrxM+VguLRsex8ViZnkb1dLkfgOyCzJtUR+IQOoHzEA6ZPu0mBGQug+ObTD+Ner19mmmFHoXzbDnvgtXfKFZtYiW1Dpg+7RYUaayZPfqe6adRrxs7mOb2Lrbk62lUj5bzLkSOMApWewGlCZwQYrEQIk8IUSiEeKyXx7OEEHVCiAP2j5/09bXe5qMiB02fdstcBl3tkLfGMe/noQaHBzIleZDejerJbDaj9dPI+RAQpjoapVbZp/kcdp0YfRNUFxn19Uxs+vAoIoJ8Wa2nUT1XYwWc2Oo106egMIETQliBfwJLgEzgbiFEZi9P3SalnGD/+EU/X+s1HDZ92m3IZAhNMP30CBi7UfPKGsgva1AdinYlij+GhnNGsmFyqw6fI3NwGCnRwY55Qz2NCoCv1cKizHg2HCvX06ie6tj7IG1etcxC5QjcVKBQSlkkpWwHXgOWueC1Hqejy8aaI6VcO8oB06fdLBbIvBEKNxhtRUxsydh4LAI9Cuep9PQpYEyf7jtde35ZgEMER0PyNcYIp8mnUZeMjaexrZPtBZWqQ9GuRM67EJUKcaNVR+IwKhO4IcCZHl8X2793oRlCiINCiNVCiO4z39fXegWHT592y7zJ2I2av9ax7+thYkMDmJIcydojpapD0frLZjNGh1IX6OlTR0+fdstcBlWFUH7Use/rYWaOjCY80Pf8edY8SEOZ0d/Xi6ZPAXwUHru3s3jhLd4+YJiUslEIcR2wHEjt42uNgwjxCPAIQFxcHNnZ2Vcab580NjY6/BjPH2kjwAqWsmNkV+Y67o2ljRl+g6jf8iw5VdGOe18Hc8Y5vdBI/w5ePtHOays3ER/s/Xt7XHFOXSG89igTG85xVKRRrvDv4w7n89UPWxgWZuHUkd2ccuD7+rZHcTUWTq36KydT7nHgO1+aO5zTC42NlKw+fJYlMTX4WjwrEXDH8+kqCWdXkSZt7G5OpMmB50D1OVWZwBUDST2+TgQ+tRVQSlnf48+rhBD/EkJE9+W1PV73NPA0wOTJk2VWVpZDgr+Y7OxsHHmMzi4b3962kYVjElh47USHve95zbcRs/+/ZM2YDP4DLDvgJI4+p71Jq23h5d9sojp4KHdljXTqsdyBK86pS6xaBVZ/Mm/6Npn+ocrCUH0+z9a2cHzNJr67KJ0sZ/z8ljxLcuMBkrOedvx7X4Tqc9obGV/O9hd2Y03IJCsjTnU4/eKO59Nlnv89RKcz5fr7HToCp/qcqhxq2A2kCiFShBB+wF3A+z2fIISIF/ZOzEKIqRjxVvXltd7io6JqqpvaHT8t0i1zGXS2QuF657y/h0iICGR8UoSeRvUkPadPFSZv7qB7d+T1zrxOVOZBuQNnADzQzJHRhAb4nC+WrHmAxgpj+jRzmVdNn4LCBE5K2Ql8DVgLHAPekFLmCCEeFUI8an/abcARIcRB4G/AXdLQ62td/7dwvpX23adZ6Q7afXqhYVdDcIxRxd7kFo+O52BxHWdrW1SHovVF8W5oLDUuzCa3+kgpmYPDSHbU7tMLjboBEMZmBhPz87GwIDOOdTmltHfaVIej9UXeKkDCqKWqI3E4pYt9pJSrpJRpUsoRUsrH7d97Ukr5pP3P/5BSjpZSjpdSTpdS7rzUa71Nl02y/mgpczNiHbf79EIWq3FxLlgH7eZu6r54TDyAHoXzFLkfgMUHUheqjkSp8oZW9p2uYdHoeOcdJDQehs4wfTkRMEY561s72Xlc70b1CLkrIGKoV/Q+vZD3r9b2YPtO11DZ2O7cCzMYIxgdzUZJERNLiQ4mIz6UNTqBc39SwrEVRqeAwAjV0Si14Wg5UsKiMU5ek5W5zNiJWpHv3OO4uWtSown199G7UT1Baz0UZUPGDV43fQo6gXNr63JK8bNanDd92m3YNRAYqe+uMUbhdp+qpqKhTXUo2qWUHzMarWd437RIf63NKWVYVBDpcU5eBzjqBuNz7gfOPY6b8/exMm9ULBuOldNlM3dtPLdXuN7oOOSF06egEzi3JaVkbU4ZV4+MIjTA17kHs/pA+nVQsB462517LDe3eEw8UsK6o3oUzq3lrgAEZFyvOhKl6ls72Hm8kkWj4xHOHmEIHwIJV0HuSucexwMszIynuqmdvadqVIeiXcqxFRAUDUnTVEfiFDqBc1O5pQ2crm5mYaaTp0+7ZVwPbXVwartrjuem0uNCSYkO1tOo7u7YB5A4xVibZWKbc8vp6JIsGu2ikhYZ18PZvVDfa9Um05iTHoOf1cK6HH2dcFsdrcba7ozrjLXeXkgncG5qXU4ZQsD8zFjXHHDEXPANMv3dtRCCRaPj+fB4FXXNHarD0XpTcwpKD3nttEh/rMspIzrEn4lJg1xzwO4p67xVrjmemwrx92HmyCjWHS1DmrzFmNs6sQXaG431b15KJ3Buam1OKVcNHURsaIBrDugbCCPmQe4qo76WiS0ZE0+nTbLhWJnqULTedN9kmHz9W2tHF9l55SzIjMPiqq4AMekQOcL0N3oAC0fHc7q6mbwyc/eSdlvHPgC/UBg+R3UkTqMTODd0prqZo+fqXTct0i1jKTSUwLn9rj2umxmXGE5CeACr9TSqe8pdAbGZEDVCdSRK7TxeSVN7l2uvE8K+7vDEVmipdd1x3dC1o2IRwhgF1dyMrQvyVkPaQvDxVx2N0+gEzg2tO2pcEFy2/q1b2iIQVmMUzsSEECzIjGN7YQUt7V2qw9F6aqqE0x+afvQNYO2RMkL9fbh6hIv7GGcsBVun6csOxYYGcNXQQXrDkzs6/RE0V3r9dUIncG5obU4p6XGhzquqfjFBkUZnBj09woLMeFo7bOwo1MU63UreKpA2069/67JP8c/NiMXPx8WX8cTJEBxr3wlsbgsz4zhytl53b3E3uSvA6m+02fNiOoFzM1WNbew5We366dNuGUuh4hhUHVdzfDcxNSWSUH8f1h/V0yNuJXclhHtnVfX+2HOymqomFxT57o3FCulL7GWHzF0vcaH9/K/Xu1HdR3eR7+FZXt8jWSdwbmbjsXJs8pMLg8tlXGd8NvkonJ+PhayMWDbmlmHTxTrdQ1sDHN9sjL55YVX1/libU2b8jDq7yPfFZCw1dvid2Krm+G4iJTqY1NiQ88teNDdw7iDUnf6k8LQX0wmcm1mbU8qQiEBGJ4SpCaC7Z5zJEziA+aNiqWxsZ/+ZWtWhaGCsuepq8/p1LZcjpWTd0VJmjYwm2N9HTRAps8EvRE+jAgtHx7HrRDW1zeYugu42cleCsBijxF5OJ3BupLGtk22FlSzIjHN+VfVLyVgKZ3ZBY7m6GNxAVnosPhahy4m4i9yVEBQFQ6erjkSpo+fqKa5pUTN92s03AEbO12WHMDabddkkm3LNfb10G3mrIWk6BLt4c48COoFzI1vzK2jvtKm9MIO9PZE0/iOYWHigL9OGR7JBT4+o19VhVFVPW+y1VdX7asPRcoSAeaNcVOT7YkbdAE3lcHaP2jgUGzsknPiwAF1OxB3UnoGyw5C+WHUkLqETODey4VgZ4YG+TEl2UVX1i4kbbUyl6mlU5o+Ko6C8kZOVTapDMbfTH0FrnZHAmdzG3DImJkUQHaK4vlXqArD4mn4a1WIxyg5tya+gtUOXHVIqf43xOc37p09BJ3Buo8smyc6rICs9Bh+r4n8WIYxp1KJsaGtUG4ti80cZu4H1NKpi+WvA6md0CzGxsvpWDhXXce0oRbvUewoIh5RZ+kYPYx1cS0cX2wp02SGl8lYbnUKiU1VH4hI6gXMT+0/XUN3U7h4XZjCmUbva4PhG1ZEolRQZREZ8qN5lplreakieBf4hqiNRqnud1Xx3uU6kXwdVhVBZqDoSpaalRBHq78NGfaOnTlsDnNxmbF4wyS51ncC5iQ3HyvGxCOakKSoLcKGk6cYddv5a1ZEotzAzjj0nq6lp0rvMlKgsgOrjpthVdjkbj5WROCiQtDg3SWTTFhmf8829XtbPx8LstBg25ZbrskOqHN8MXe2mWmahEzg3sfFYGVOSIwkP9FUdisHqAyMXGAmcyXeZzc+MwybRu8xUybO3dutOFkyqtaOL7YWVzB+leJd6TxFDIXa0vtHD6I1a3tDGkZI61aGYU95qY9DBRLvUdQLnBk5XNVNQ3si1qneVXSh9idFP7uxe1ZEoNXZIOHFh/nodnCp5ayBujJEsmNiOwkpaO2xueJ1YDKd2QkuN6kiUykqPxSKMYuyai9m6oGAtpC4Eq5sMgriATuDcwMZcIzFwm3Ut3UZeazS3797ZY1JCCOaP0rvMlGiuhjMf6elTjGUWIf4+TEuJUh3Kp6UtBtkFheZeLxsZ7MdVQwedv55rLlS8B5qrTDV9CjqBcwsbj5UzIibY9c3rLydwEAydYfoEDmBBZhzN7V18WFSlOhRzKVhvNK83SVmAi5FSsim3jNlp0a5vXn85QyZBULS+TmDU5jtytp7SulbVoZhL/mqw+BjFpU3Eza4E5tPQ2sGuE1XuN/rWLW0RlB0xCiSa2IwRUQT7WXVRX1fLXw0hcZAwUXUkSh05W09ZfRvXZrjhdcJiNaauCtZDV6fqaJTqvo7r9bIulrfaGGwIjFAdiUvpBE6xrfmVdHRJ9ykfcqHuIWmT3137+1iZnRbDxmPlSKl3mblEZ7sxLZe6ECzmvlRtOFaGRcDcDDdb/9YtfTG01hot+EwsNTaExEGBupyIK1WfgIpco6SNyZj7qugGNh4rIyLIl6uGRqgOpXfRqRA5XO8yA+ZlxFJa38rRc/WqQzGH0zuhrV6vf8NYJ3vV0EFEBvupDqV3w+caXRlMfqPXvV52e2ElLe16vaxLdP/MmaR9Vk86gVOoyybZnFfO3PRY9d0XLkYIYxTuxFZoN3c7qax0Y/Rjs54ecY28NWD1h+FZqiNR6lxdC0fO1rvvKD1AQBgkX2P6BA6MciJtnTZ2HtddGVwibxVEpxsDDSbjplmDOew/XUNNcwfz3HVapFvaIqMrQ1G26kiUign1Z3xiuF7f4gpSGuvfhs8BPzfb3ONi3WUp5rtb+ZALpS2GynyoOq46EqWmpkQS7Gdlo75OOF9rnVHCxqSj9DqBU+h894V0N+m+cDFDrwb/MH13DczLiGP/mVqqGttUh+LdKvKg5qTpygL0ZuOxMoZGBjEy1k26L1zM+a4M5l5u0b1edpNeL+t8hRvA1qkTOBWEEIuFEHlCiEIhxGO9PP45IcQh+8dOIcT4Ho+dFEIcFkIcEELscW3kjrHxWBlTUyIJC3DzwoM+9ibiuisD8zJikRK25FeoDsW7dbdmMnkC19zeyY7jVVw7KtZ9ui9cTGQKxGToGz0+WS+bU6LXyzpV3hoIioLEKaojUUJZAieEsAL/BJYAmcDdQojMC552ApgjpRwH/BJ4+oLH50opJ0gpJzs9YAf7pPuCG69r6Sl9CTSWwbkDqiNRanRCGDGh/noa1dny1kD8OAgfojoSpbYXVNLeaXPfMkMXSlsEp3YYU1smNjcjFqG7MjhXVycUrLPvUreqjkYJlSNwU4FCKWWRlLIdeA1Y1vMJUsqdUsru/iwfAYkujtFputsyuf26lm4jFwDC9HfXFotgXnosW/Ir6Ogy92ik0zRVGeUoTDot0tPGY+WE+vswJTlSdSh9k7bEmNI6vkl1JEpFh/gzISmCTborg/MU7zZK15i4R7LKBG4I0LM6bLH9exfzILC6x9cSWCeE2CuEeMQJ8TnVxtwyRsaGMCzKQxZoB0dB0lTTJ3Bg3F03tHay95S5ez86TeEGQJr6wgxG94XNeeXMTotxv+4LF5M4xejgkqevE/NHxXGwuI7yet2VwSkK1hmtHkfMUx2JMj4Kj93bgo5eV3wKIeZiJHDX9Pj2TClliRAiFlgvhMiVUm7t5bWPAI8AxMXFkZ2dPeDAL6WxsfGyx2jplHx0vJmFyb5Oj8eRhvqkMfzMf9m59m3a/V3Xj7Ev59SVZKfEKuDF9XtpTXfTulyX4W7ntKdRR19ikG84O/ProCBbdTh94ozzeaq+i/KGNgZT5bb/Vr3JCBtP1NGV7Bi00fgFe4Xc+We0L8IajRH6J97fxpxE9eucPf18Xmjy/nfpDMvgwEf7lcWg+pyqTOCKgaQeXycCJRc+SQgxDngWWCKlPN+IUkpZYv9cLoR4F2NK9jMJnJTyaexr5yZPniyzsrIc+Ff4rOzsbC53jLU5pXTJvdw/fxIzRrhZY+pLKYuFJ/7L1VH1MPlWlx22L+fU1Wac3EVBfStZWXNUh3JF3PGcAmDrgl2fh8zryJrrOXfWzjif/9xcCOTxpRtnExPq79D3dqroKngrm6wRwTB0+hW/jdv+jPaRlJInczZTbAsjK0v9Mm1PP5+fUl8C2Sdg/s/IuiZLWRiqz6nKcfndQKoQIkUI4QfcBbzf8wlCiKHAO8B9Usr8Ht8PFkKEdv8ZWAgccVnkA5SdV06Ivw+TkwepDqV/YkdBxFA9jYqxy6ywvJEz1c2qQ/EuZ/dCSw2kLlAdiXKbc8sZOyTcs5I3MBqKW3xMf50QQjAvI5btBZW0dequDA5VuMH4nLpQbRyKKUvgpJSdwNeAtcAx4A0pZY4Q4lEhxKP2p/0EiAL+dUG5kDhguxDiIPAxsFJK6RFXCyklm3MrmJUaja+7dl+4GCEgdREUbYEOc6/r6C6+rHejOljBOhAWozWTidU1d7DvdA1z3b1GZG8CwiFpOhRsUB2JcnMzYmjp6OLjE9WqQ/EuBesgbAjEXli4wlyUZhBSylVSyjQp5Qgp5eP27z0ppXzS/ueHpJSD7KVCzpcLse9cHW//GN39Wk+QV9ZAaX0rc9M9ZPfphVIXQmeLUSrAxJKjgxkeHayrrTtawXpInApBHrLr0km2FlRgk5Dl7l1aLiZ1AZQdNqa6TGzG8Gj8fCxsztV1Ix2msx2OZxsjve5eG9HJPGwIyPN1/0d2++4LF5N8DfgEGL9oTW5eRiwfFVXR3N6pOhTv0GCvM6inT9mcV86gIF/GJ0aoDuXKdE9tmfw6EehnZcbwKLLz9I2ew5zZBe0Npp8+BZ3AudzmvHIyB4cRFxagOpQr4xcEybOMIWyTm5cRS3unjR2FVZd/snZ5el0LADabZEteBbPTYrBaPHSEIXYUhCXq6wQwNz2GosomTlY2qQ7FOxSsA4uv0SfZ5HQC50J1LR3sPVXD3AwPHX3rlroQqo+bvmn15ORIQvx9dLFORylYByHxED9WdSRKHSmpo6qp3XOXWYB9vewCKMo2prxMLMv+76hH4RykYD0Muxr8Q1VHopxO4Fxoe0ElXTbp2Rdm+GSKy+TTI34+FmanRbM5t0I3rR6ork44vhlS9bqWzbkVCAGz07zgRq+9EU5/qDoSpbrXy27O0+vgBqz2NFQc08ss7HQC50LZeeWEB/oyISlCdSgDE5kCUal6egSYm240rT56TjetHpDij6GtzvTTp2AssxifGEFksGcWiT4vZTZY/fR1AmMU7sOiKlradTmRAekeNNDXCUAncC5js0my8411LT6eVj6kN6kL4OR2aDf3uo7u6ZHNejfqwBSsM2qHDc9SHYlSVY1tHCyu9fxRegD/EGOqy+Qj9WCUE2nvtPFhUaXqUDxb4QajFml0mupI3IIXZBKe4ei5eioa2sjy9GmRbqkLoKsNTmxTHYlSMaH+jE+K0OVEBqpgg1E7LCBcdSRKbSuoREo8f51st9SFUJkHNadUR6LU1JRIAn2tZOtp1CvX2WasqUxdaPplFt10Auci3SM0Hls+5ELDZoJvkJ4eAbLSYjhwppaaJnMv1r5i9SVGzTC9roXNeeVEh/gxJsFLEtnuqa5Cc4/C+ftYmTkymk255Xq97JU6tQM6mvX0aQ86gXMRY11LONEhHtYW52J8/I3prsL1YPILUlZ6DFIaxVe1K6DXtQDQZZNssS+zsHhq+ZALRY2EQcl6GhVjVLW4poXjFeZednLFCtaD1d8oY6UBOoFziZqmdvafqT2/XsprpC4wdgVV5l/+uV5snH3B+RY9PXJlzrfFGaU6EqUOFtdS29zhHevfuglhJOa6/Z4uJzJQBeuNQvJ+QaojcRs6gXOBrQUV9nUtXnRhBhjZXU7E3NOoVotgdmo0W/IrsNnMPRrZb53txi/31AWmX9eSnVuORcDsVC9ZZtHtfPu97aojUWpIRCBpcSFs1glc/1UXQVWB6UfpL6QTOBfIzqsgMtiPcUO8ZF1Lt4gko5mwyRM4MO6uq5raOXy2TnUonuXMR7otjt3mvAquGjqI8CBf1aE4lm6/d97c9Fg+PlFNY5tuv9cvBd1dWvQ62Z76lMAJIYKEEP8nhHjG/nWqEGKpc0PzDt3rWuZ407qWnlIXwKkPodXcddBmp8UgBHqXWX91t8VJMXdbnPKGVg6frfO+UXoA30CjJpy+0SMrPZaOLsmOQl1OpF8K1kHkcIgaoToSt9LXEbjngTZghv3rYuBXTonIyxwqrqW6qZ0sb9l9eqHUhWDrgBNbVEeiVGSwH+MTI8jO19Mj/VKwwd4WJ0R1JEptzTd+oXv1daK6SLffSx5EiL+PXgfXHx0tcHKbHqXvRV8TuBFSyt8BHQBSyhbAC4eTHG9zXoV3rmvpljQN/MP03TXGL98DZ4yEXeuD821x9IV5c145saH+ZA4OUx2Kc4ycb3w2+XXC12phVqpuv9cvJ7dDZ6uePu1FXxO4diFEICABhBAjMEbktMvYklfOxKGDGOTpbXEuxuoLI+Ya61tMfkGamx6LlLBNlxPpG10+BIDOLhtb8yvISo9BeOtGDt1+77zu9nu5pQ2qQ/EMBevAJxCGXaM6ErfT1wTup8AaIEkI8TKwEfie06LyEhUNbRwsrmOut06LdEtdCA3noOyI6kiUGjsknKhgP70Orq8K1tvb4qSqjkSpfadraWjt9K7yIb1JXQgnd5i+/V53MXe9G7UPpDQSuOFzwDdAdTRup08JnJRyPXAL8HngVWCylDLbeWF5h635xi9yr6v/dqHz0yPm3mVmsQhmp8XociJ90dlmrJvUbXHIzivHxyKYmRqtOhTn0u33AIgLC2B0QhjZufpG77KqCqHm5Ce/Y7RPuWQCJ4S4qvsDGAacA0qAofbvaZewOa+cGG9e19ItNB7ix5k+gQNjHVx1UzuHdDmRS9Ntcc7bnFfBpGGDCAvwsvIhFxp2NfgG62lUjGnUvadrqGvuUB2Kezu/zEKvf+vN5Ubg/mj/+CewC3gaeMb+5785NzTPdn5di7eWD7lQ6kI4swtaalRHotTs1O5yInp65JJ0WxwASutaOXau3jvLh1you/2eXi/L3IwYumySbYV6FO6SCtZBdLrRjk37jEsmcFLKuVLKucAp4Cop5WQp5SRgIlDoigA91YEztdS3dprjwgxGAie74Phm1ZEoNSjYjwlJEWzW6+AuTbfFAWCLveyM169/65a6AOpOQ0We6kiUmpA0iIggXzbradSLa2s0Rur16NtF9XUTQ4aU8nD3F1LKI8AEp0TkJTbnlWO1CK7x9nUt3RInQ+AgPY0KZKXFcqi4lqpGvVG7V7otznmbcytICA8gLc4kdfBSdfs96G6/p9fLXtKJrdDVrhO4S+hrAndMCPGsECJLCDHH3pHhmDMD83Sbc02yrqWbxQojroXC9WCzqY5GqbkZMfZyIrraeq90WxwA2jttbC+sZE56rPeWD7lQeCLEjjZ9AgfGetnKxjZySszdxeaiCteDXwgMnXH555pUXxO4LwA5wDeBbwFH7d/TelFa18rRc/XmmRbplroQmirg3H7VkSg1JiGc6BA/XSbgYgrWQeQI07fF2XPK6Inp9WWGLpS6AE7r9ntz7O33NuXq68RnSGnM5gzPMtZOar3qaxmRVinln6WUN9s//iylbHV2cJ7q/LqWDJNdmEdeC4hPRlhMymKfHtmaX0GXnh75tPNtccw9+gawJa8CX6tg5kiTLLPolroAbJ1QlK06EqWiQvwZp9vv9a4iF+rO6OvEZfS1mf0JIUTRhR/ODs5Tbc6tYHB4AOlxoapDca3gaBgyyRj6Nrk56THUNHdwqLhWdSjuRbfFOW9zXjlTUyIJ9vdRHYprdbff09cJ5ur2e73rnmIfqa8Tl9LXKdTJwBT7xyyMEiIvOSsoT9Zpk2wvrCTLTOtaekpdAMV7oKlKdSRKzU6NwSLQu1EvpNviAFBc00x+WaP5llmAbr/XQ3f7ve6i75pdwXpjrWT4ENWRuLW+TqFW9fg4K6X8CzDPuaF5poIaG41tnWSZbV1Lt9QFgITjG1VHolR3OZEteh3cJ7rb4qTMNn1bnO52a17fpeVidPs9oGf7PX2dOK+13lgjqUfpL6uvU6hX9fiYLIR4FBjw/KAQYrEQIk8IUSiEeKyXx4UQ4m/2xw/17P5wudeqcqiyy5zrWroNnghB0XqXGcYv50Nn66jU5UQMVceNtjj6wkx2XgVJkYGMiAlWHYoauv0eYKyXnWNvv6fXy9oVZRtrJHWZocvq6xTqH3t8/Bq4CrhjIAcWQlgxOjwsATKBu4UQmRc8bQmQav94BHiiH69V4lBFJ1NTIgkx27qWbhaL8Qu6cCPYulRHo5SeHrlAd1Jv8gSurbOLHYWVZKWZdJkF6PZ7PWRlxFLT3MFBvV7WULAO/MMhaarqSNxeXxO4B7u7MkgpF0gpHwEGuupyKlAopSySUrYDrwHLLnjOMuA/0vARECGEGNzH17rc2doWzjZKc65r6WnkfGiphrP7VEei1OiEMKJD/M5Pl5mebosDwMcnqmnp6DLfLvUL6fZ7AMxOjcYi0NcJMJZZFG6AEVnGWkntkvqawL3Vx+/1xxDgTI+vi+3f68tz+vJal+tex2DadS3dRswDYTH9NKrFIpidFsPWAj09QnuTbotjtzm3Aj8fCzOGm3SZRTfdfg+AiCA/Jg4dpNfBgbEmsuGcnj7to0vO8wkhMoDRQLgQ4pYeD4UBA12F3NvcwYW/5S72nL681ngDIR7BmH4lLi6O7OzsfoTYP531XSxJkpzJ2U3xUZNOjdhNDE3Hsu9t9lpmDvi9Ghsbnfrv5kxxXZ3UNnfw/HubGDnIqjqc81x9TqMqP2ZsVzsHmmOp9dB/y0vpz/lcdaCZ9AgLu3Zuc25Q7k52MdMnhMrt/yWvMvIzD3vy//v+GubXzjsFHby3djPh/s753eEJ53PoqbcYDuwsD6LdzWMF9ef0cgu10oGlQARwQ4/vNwAPD/DYxUBSj68TgZI+PsevD68FQEr5NPA0wOTJk2VWVtaAgr6cYdnZOPsYHsFyG2z6JVmTMyFkYCOS2R58Tic0t/PUofXUByeSlZWuOpzzXH5OV7wHfiFMuOFRr6ys3tfzeaqqidI12XxpXjpZM1OcH5i7q1rE4BPbGDx7trF+tgdP/n/fX9GpdbxTsJ2O6FSyJiU65RgecT7//RsYPJ6rF91y+ee6AdXn9JJTqFLK96SUXwCWSim/0OPjG1LKnQM89m4gVQiRIoTwA+4C3r/gOe8D99t3o04H6qSU5/r4Wk2l7qmyQnN3ZTg/PWLmjQxSGt05dFuc8+ucTL9OtlvqQmgqh9KDqiNRanRCGDGh/uaeRm2pMdZE6unTPrtkAieE+J79j/fYy3l86mMgB5ZSdgJfA9YCx4A3pJQ5QohH7WVKAFYBRUAh8AzwlUu9diDxaA4WPw5C4k2/Dg4gKy2GQ8V1VDSYtJxIRR7Unf6kdISJZeeVkxIdTHK0ScuHXGjEtcZnk+9GFUKQlWa03+vssqkOR43jm0HadPeFfrjcJoZj9s97gL29fAyIlHKVlDJNSjlCSvm4/XtPSimftP9ZSim/an98rJRyz6Veq7kRISB1PhzfBF2dqqNRam6GMdpi2nIiunwIAK0dXew8XsWcNJPvPu0pJAYSrjJ9AgfGdaK+tZP9Z2pVh6JGwXoIHASJk1VH4jEuN4X6gf3zi719uCZEzWOlLoTWOijerToSpTIHhxEd4m/eadSCdfa2OM5Z2+MpPiyqoq3Tdj6h1+xSFxrXCJO335s5MhqrRZhzGtVmM3rjjrgWLO6z2cvdXW4K9QMhxPsX+3BVkJqHGp4FFh/TT6N2V1vfasZq6631cPoj04++AWTnlhPga2Faymd3XJpa6kKM9nubVEeiVHigL5OGDWJzrglv9M4dgKYKvf6tny63C/UPLolC804B4ZA03Rgan/9T1dEoNTcjhrf3FXPgTA2ThpnoF/iJLWDrMH0CJ6UkO7+Cq0dEE+CrRxg+JWEiBEUZN3rjblcdjVJz02P57ZpcyupbiQszUb/gwg2AgJHXqo7Eo1xuCnXLpT5cFaTmwVIXQNlhqO+1yotpzBoZY85q6wXrwD8MkqapjkSpE5VNnKpq1tOnvbFYjA0ux3X7ve7uHFvMeJ1ImAjBJi9u3U99bWa/VAixXwhRLYSoF0I0CCHqnR2c5gW6h8RNXk4kPMiXq4YOMlcCJ6Ux+jpirunb4my2/7tn6Q0MvUtdCM1VULJfdSRKpceFEh8WwGYzrYNrqoLiPZC2SHUkHqevrbT+AjwAREkpw6SUoVLKMOeFpXmN2FEQNsT06+AAstJjOHy2jvKGVtWhuIZui3Nedl45I2NDSIoMUh2Ke9Lt9wCjnMjcjBi2FVTSYZZyIsc3AtL0yyyuRF8TuDPAESmlyVZgawMmhPEf83g2dLarjkap7h65W/MrFUfiIt2/jE1e/62prZNdRdXMTdejbxcVFAlDJps+gQPjOtHY1smekzWqQ3GNgnUQFA2DJ6qOxOP0NYH7HrBKCPEDIcS3uz+cGZjmRVIXQnuDUWXbxLqrrZtmeqRgPQweD6HxqiNRaufxKtq7bLr7wuWkLjSmUBtN8v/jImaOjMbXKsjON8F5sHUZy2tSF3ymlZp2eX09Y48DzRgN7EN7fGja5aXMAYuv6e+uu6utbzNDtXXdFue8zXnlBPtZmZxsot3HV+J8+72NauNQLMTfhynJkWSboZzI2b3GtUJPn16RviZwkVLKW6SUP5VS/rz7w6mRad7DPwSGXa2rrfNJtfV9p2tVh+JcxzcZbXFMnsBJKcnOLeea1Gj8fPQIwyXFj4OQONPf6IFRTiSvrIGS2hbVoThXwTpj7eOIeaoj8Uh9vaJsEEKY+0qsDUzqQqg4BrVnVEei1DWp0fhYhPdPoxZsMNriDJmkOhKl8ssaKalr1dOnfXG+nIhuv9ddTsTrd60XrDNKDAUOUh2JR+prAvdVYI0QokWXEdGuyPlyIuYehQsL8GVy8iA253pxAtfdFmfkfNO3xelO1LN0Atc3qQugtRbO7rnsU73ZiJgQhkQEeveNXkMpnDuop08HoE8JnJQyFIgGsoAbgKX2z5rWN9GpEDFMT6MC8zJiyS314umR7rY4I/WFOTuvnFGDw4gPN1FV/YEYPheE1fTTqN3lRHYUVtLW6aXFjbtrg5p8mcVA9LWQ70PAFmAN8DP75584LyzN63SXEynKhs421dEo1T2d5rV31wXr0W1xoL61gz0na3T5kP4IjDCm1EyewIFxnWhu72L3CS8tJ1KwHkIHQ9wY1ZF4rL5OoX4TmAKcklLOBSYCJilmpTlM6kLoaIZTO1RHotTI2BASBwV6b9PqgnXG2jeTt8XZUVBJp03q9ln9lboASg/j11alOhKlZoyIws/HQrY33uh1dcDxzca/tRCqo/FYfU3gWqWUrQBCCH8pZS6Q7rywNK+UPAus/sYCdxMTQjA3PZYdhZW0dnjZ9EhTpVEaQE+LsDmvnLAAHyYmRagOxbPYf3Yiq83dVivIz4dpKZHeOVJ/5mNoq9PXiQHqawJXLISIAJYD64UQ7wHm7k6u9Z9fEKTM0tMjGOvgWjq6+PhEtepQHKtQt8UBo3zI5rwKZqXF4GPV5UP6JW40hCYQVWXujQxgTKMer2jiTHWz6lAcq2CdURs0ZY7qSDxaXzcx3CylrJVS/gz4P+A54CYnxqV5q5ELoKoAqotUR6LU9OFR+PtY2ORtu1EL1kFwDAyeoDoSpXJK6qloaNPlQ66EEJA6n0E1B42pNhPrnn73umnUgvUwbAYE6JbqA9HvW0Mp5RYp5ftSSnM3ttSuTPfIjMmnUQP9rFw9Isq7LszdbXFG6rY43f+uc9L0BoYrkroQn65m07ffS4kOJjkqiM3eVA+urhjKc/QudQcw91VWc72oERA5wvT14MC4uz5Z1cyJyibVoThG8R6jhpfJp08BNudVMC4xnJhQf9WheKaUOdiEj15ugVFDcOdxL1ov211KSq9/GzCdwGmul7oQTmyFDi+tg9ZH3dNrXjONWrDOqOE1Yq7qSJSqaWpn/+kaXbx3IALCqAvP1HUjgaz0GFo7bHxU5CW7cgvWQ/hQiNH7IAdKJ3Ca66XOh85WOLlddSRKJUUGMTI2xHumUXVbHAC2FlRgk+j6bwNUHXkVlB81ptxMbPrwKAJ8Ld7RVquzzagFqsuHOIRO4DTXG3YN+ATq6RGMX/K7iqppavPw3o/156D0kJ4+BbbkVRAZ7Me4xAjVoXi0qih7H12Tj8IF+FqZMdxL1sue2gkdTXr61EF0Aqe5nm8ADJ9jJHBSqo5GqbkZsbR32dhR6OF1sc+3xTF3AmezSbLzK5iTFoPVokcYBqI5KMmYajN5AgdetF62YL1RCzRllupIvIJO4DQ1UhdAzUmoOq46EqUmD4skxN/H84t1FqzTbXGAQ2frqG5qJ0tPnw6cbr93Xlaal5QTKVgHydeAX7DqSLyCTuA0Nbq3kJt8GtXPx8Ks1Gg251YgPXU0sqtDr2ux25xbjkXA7FSdwDlE6gJjyu3UTtWRKDU0KogRMcGeXU6k+oRRA1RPnzqMTuA0NQYNg+h00ydwYOxGLa1vJbe0QXUoV+bMLmir1xdmjBGSiUMHMSjYT3Uo3iFlNlj9PpmiN7Gs9Fg+Kqqiud1D18vqZRYOpxM4TZ3UBUZj+3YPX9cxQN3TbR5bTkS3xQGgoqGNg8V1ZOnivY7jF2xMuekbPeamx9LeaePD4x5aTqRgnVEDNGqE6ki8hpIETggRKYRYL4QosH/+TN0BIUSSEGKzEOKYECJHCPHNHo/9TAhxVghxwP5xnWv/BppDpC6ErnajJpyJxYYFMGZImOeub8lfp9viAFvzjemt7vZHmoOMXACV+cYUnIlNSRlEkJ/VM8uJdLQY13k9Su9QqkbgHgM2SilTgY32ry/UCfyvlHIUMB34qhAis8fjf5ZSTrB/rHJ+yJrDDZ0BfiH67hrj7nrvqRpqmz2sQ13NKag4pi/MGCOoMaH+ZA42dyLrcN0/WyafRvX3sTJzZDSb88o9b73siW1G7c/U+aoj8SqqErhlwIv2P78I3HThE6SU56SU++x/bgCOAUNcFaDmAj5+MDzL2FruaRckB5ubEYtNwtYCDysnkr/W+Jy2RG0cinXaJFvzK7g2IxaLLh/iWFEjYFCKLieCsdyiuKaF4xWNqkPpn/zVxs16si4f4kiqErg4KeU5MBI14JJzDkKIZGAi0LOz8deEEIeEEP/ubQpW8xCpC6DuDFTkqY5EqfGJEUQG+7HZ09bB5a+BqJEQPVJ1JErl19hoaOvk2lFxqkPxPkLo9nt23e3ZNud60DSqlMaN3oi54KN7AzuSj7PeWAixAYjv5aEf9fN9QoC3gW9JKevt334C+CUg7Z//CHzxIq9/BHgEIC4ujuzs7P4cvt8aGxudfgxv4t8awgzg+Jp/cWboLb0+xyznND28iw1HzrIptgaLk8txOOKcWjubmVm0hbNDrue4Cf59LmX32RZ8LAJbyVGyy4+pDscr9PwZjWyJZ1xnC4fe/yfVUZPVBqZYYojgnY/ySLWd7tfrVF1HQxqKmFx/ltzBt1DqZdcJ1b+bnJbASSkvOtkthCgTQgyWUp4TQgwGeh12EEL4YiRvL0sp3+nx3mU9nvMMsOIScTwNPA0wefJkmZWV1d+/Sr9kZ2fj7GN4nRN/YURXISMuct7Mck7rIs7yzdcOMGjEBCYOde6gskPO6bEPQHaSdO3DJJm4srqUku9tXc2s1GgWzZ+qOhyv8amf0Y7pkPsHxvmfhazvKI1LtRtbc3l6axETp80kPNC3z69Tdh3dshsQZNzwDTJCvGuDj+rfTaqmUN8HHrD/+QHgvQufIIQQwHPAMSnlny54bHCPL28GjjgpTs0V0hfD6Q+huVp1JErNSYvBIvCcadS8NeAfDkOnq45EqeMVjZQ3S+bp6VPn8Q0wpuDy15p+vey1o+LotEm25HvINGr+ahgyCbwseXMHqhK43wALhBAFwAL71wghEoQQ3TtKZwL3AfN6KRfyOyHEYSHEIWAu8D8ujl9zpLQlIG2mX6QcEeTHVUMHsdETEjibDQrWGrvKrH0fBfBGG48Z/17X6vIhzpW2GOrPQukh1ZEoNSEpgqhgPzYeK7v8k1VrLIeze42bdM3hnDaFeilSyirg2l6+XwJcZ//zdqDXhUBSyvucGqDmWgkTISTOuFMbf6fqaJS6dlQcv12Ty7m6FgaHB6oO5+JK9kFThfFL1eQ2HisnKdRCQoQb/3t5g7RFgDBGfgePVx2NMlaLYG5GLOuPltHZZcPH6sb1+M/vUtfXCWdw4395zTQsFmOXWeFG6PSwOmgOtiDTGMXpHtVxW/lrQFhgpLnrOtU2t7PnVDUTYq2qQ/F+IbHGVFz+atWRKDd/VCx1LR3sOVWjOpRLy18DYYkQN0Z1JF5JJ3Cae0hfYvTTPG3uptUjYkIYFhXEBnefHslfA0nTIShSdSRKZedVYJMwIUYncC6RvhhK9kP9OdWRKDUrNQY/q8W9p1E7WuH4ZmPk1Mm76s1KJ3CaexieBT4BxvSIiQkhmD8qjp2FVTS1uWnT6rpiKD2s17UAG3PLiQ7xIyVcX0pdIt2+DLpgrdo4FAv292H6iCj3Hqk/uR06moybc80p9FVHcw9+wUYz9PzVpt9lNn9UHO1dNra5a1cGva4FgI4uG9l55cxNj3V63T7NLjYTwoea/kYPjGnUosomity1K0P+GvAN0t0XnEgncJr7SF8MNSdN35VhcvIgwgJ83HcaNX+N0dooOk11JErtOVlDQ2sn147Su09dRgjjOlGUbfquDPMy3Hi9rJTGdWL4XKMEjOYUOoHT3Ef3iI7JFyn7Wi3MzYhlc245XTY3G41sb4KiLca/lclHnTYeK8PPauGa1BjVoZhL2mLobDF+Dk0scVAQGfGh7nmjV37UaJGYtkh1JF5NJ3Ca+whLMMoD5Jk7gQOjnEhVUzsHzrjZLrOiLdDVpte/AZtyy5k2PJIQfyXVmMwr+RqjMbrJb/TAWG6x51QNdc0dqkP5tO5ruE7gnEoncJp7SVsCZz6GJjdd/+Uic9Ji8LEI1h91s+mR/DXgHwZDr1YdiVJFFY0UVTYxX3dfcD0ffxgxT3dlAK4dFUuXTZKd727XibVGfc/Q3tqha46iEzjNvaQvBiQUrFMdiVLhgb5MGx7pXmUCbDbjwjxiHvj4qY5GqU32bhnzdPcFNdKXQMM5OHdAdSRKjU+MIDrEnw3utA6usQKKdxs345pT6QROcy+DJ0DoYD2NClybEUdBeSMnK5tUh2IoPQiNpabffQqw4VgZ6XGhJEUGqQ7FnFIXcr4rg4lZLIJ5GTFk55XT0WVTHY6hcD0g9fSpC+gETnMvQhj/8Y9vgs421dEo1T095zaLlPNWG90XUheojkSpuuYOdp+sYZ7efapOcDQkTdXr4DDWyza0drL7RLXqUAx5q42bcBO3O3MVncBp7idtCbQ3GoUgTWxoVBBpcSHuUyYgdyUMnWH88jSxTXlldNkkCzP1+jel0hbDuYNQX6I6EqVmpUbj52Nxj2nUjhajJWL6dabfpe4KOoHT3M/wOeATaCyYN7n5o+L4+GS1+l1m1Seg7AhkXK82DjewLqeM2FB/xidGqA7F3Lor/Jv8OhHk58PVI6LYmFuGVL2po2iL0X1BXydcQidwmvvxDTRaa+WtMf0us/mZce6xyyxvlfG5u5WRSbV2dLElv4IFmXFYLHqEQamYDBiUrNfLYkyjnqpqprBccVeG3BXGLnXdfcEldAKnuaeM66DutNFz08QmJEYQHeKnfnokdyXEjYHIFLVxKLajsJLm9i4WjtblEZQTAtKvN7oytNarjkapBfb1suuOKlwva+sykunUhabfpe4qOoHT3FP6dcaC+dwVqiNRythlFqt2l1lTJZz+UE+LYEyfhvr7MGN4lOpQNIBRS6GrHQo3qI5EqfjwACYkRbA2p1RdEGc+huZKfZ1wIZ3Aae4pONpYMH/M3AkcGOvgGlo72VWkaJdZ/hqQNtNPn3bZJBuOlZGVEYufj750uoWkaRAUbfobPYBFo+M5VFxHSa2iHrG5K8DqByPnqzm+CemrkOa+MpZCeQ4BLedUR6LUrNQYAnwt6u6uc1dCWKLpywLsO11DVVO73n3qTixWYzND/jrTlx1aONo+jariOiGlcZ1ImQMBYa4/vknpBE5zX/ah+JiKjxQHolagn5WstFjWHS3F5urm9u1NRk2+jOtNXxZgXU4pvlZBVrpuXu9WRt0A7Q1wYqvqSJQaERPCyNgQ1uYoWAdXfgxqTujpUxfTCZzmvgYNg/hxRFeaO4EDWDQmjrL6Ng4U17r2wMc3QWer6S/MUkrWHS3j6hHRhAb4qg5H6ylljtHcXk+jsmi0UXaopqndtQfOXQEI0y+zcDWdwGnubdQNhNXnQYObdCNQZF5GHD4WwdojLp4eyV0JAREwzNzN6wvKGzlV1Xx+mkpzI74BRneQ3FXGTkgTWzQ6ni6bZGOui3et566AxCkQqv9/uJJO4DT3lrEUgYS8laojUSo80JerR0azJqfUdcU6uzqNsgBpi8Fq7lGn7nVF3eUaNDeTsRSayo0m6iY2dkg4CeEBrl0vW3vG6Ihh8lF6FXQCp7m32FE0Bw7Wu1GBxaPjOVXVTF5Zg2sOeHontNbqCzNGfa2JQyOIDQtQHYrWm9QFYPGFYx+ojkQpIQQLR8ezNb+C5vZO1xy0u8h3xlLXHE87TydwmnsTgsro6cYC5dY61dEotSAzDiFgjaumUXNXgk8AjLzWNcdzUyW1LRwqrmNhpi7e67YCwo0WfLkrTN+9ZWFmHG2dNrbmV7jmgLkrIDodoke65njaeTqB09xeZfR0sHUYpQJMLCbUn8nDBrkmgesuCzB8LvgFO/94bmzDMWP95SK9/s29ZSyFmpNQflR1JEpNTYkkIsjXNbtRm6vh5A49Sq+ITuA0t1cflgYh8ZBr7ukRMBYp55Y2cKqqybkHOncA6s7oCzPGiOfI2BCGx4SoDkW7lIzrAWH65RY+VgvXZsSx8ViZ87u35K8F2aWvE4roBE5zf8Ji9EYt2AAdiqqMu4lF9h6cTl+kfPQ9sPiY/sJc2djGR0VVXDdGT5+6vZBYozODvtFj0eg46l3RveXoe0aR7yGTnHscrVc6gdM8Q8ZS6GgyGlebWFJkEKMTwpw7jSol5CyHlNkQFOm843iAdTll2CQsGTtYdShaX2RcD6WHjalUE5udFkOgr9W5N3qtdXB8I2QuM32Rb1WUJHBCiEghxHohRIH986CLPO+kEOKwEOKAEGJPf1+veZHkWeAfbvpdZmDsRt13upay+lbnHKD0sFFVPXOZc97fg6w+co6U6GAy4kNVh6L1xSj7TkiTXycCfK1kpcewJqeULmd1b8lfC13t+jqhkKoRuMeAjVLKVGCj/euLmSulnCClnHyFr9e8gY+fMY2auwI6XVxl3M0stk/nrTvqpEXKR98DYYWMG5zz/h6iuqmdnceruG5sPEKPMHiGyOFGz96c5aojUe66sYOpaGhjz0knTaPmLIfQBKOAr6aEqgRuGfCi/c8vAje5+PWaJ8q8yRi2P7FFdSRKGQvqg1lz5Jzj31xKOLockq+B4CjHv78HWX/UGL1YMkZPn3qUzJvg7B6oPa06EqXmZcTi72Nh1WEnXCfaGqBwA2TeCBa9EksVVWc+Tkp5DsD+OfYiz5PAOiHEXiHEI1fwes2bjJhrTKPmvKs6EqWEECweHc9HRdVUNbY59s3Lj0JVoZ4WAVYdLmWofc2h5kFG32R8Pvqe0jBUC/b3YV5GLKuOOGEaNX8tdLUZybKmjI+z3lgIsQHobevWj/rxNjOllCVCiFhgvRAiV0q5tZ9xPAI8AhAXF0d2dnZ/Xt5vjY2NTj+G2fQ8pxkRk4g6spydYTcjLeZt7xTX3kWXTfK3d7Yyd2j/z8PFfk6TT7zCMCzsrImiw8Q/x43tku0FzSxK9mXLlsuP+Or/9443kHM6KWQE8sMX2dc+1rFBeZhkayerG9p4dvkmhvi1OOxndPSRZwnzG8SHRS1wwjHv6YlU/793WgInpZx/sceEEGVCiMFSynNCiMFAr513pZQl9s/lQoh3ganAVqBPr7e/9mngaYDJkyfLrKysK/479UV2djbOPobZfOqcJrTBK5uYkyghLUtlWEpJKXkxfwsFbQH8PGt6v19/0Z/TI9+D5JnMXHjTgGP0ZG/uOUOXPMSj109lXGLEZZ+v/9873oDOqc99sOFnZI1PgUHDHBqXJ5nS1snzR9dz1hpHekilY35G2xph+3646n6y5s4b+Pt5MNX/71VNob4PPGD/8wPAZ8a6hRDBQojQ7j8DC4EjfX295qWG62lUMKZRl44bzEdFVVQ0OGgatTwXKvP09Cmw6vA5EgcFMnZIuOpQtCvRPbWnp1GZmx7L6iOl2BzVYqxgHXS26uuEG1CVwP0GWCCEKAAW2L9GCJEghLB3xiUO2C6EOAh8DKyUUq651Os1E/DxM0oF5K6ETgev//Iw149LwCZx3GaGo+8BAkaZe/dpXUsH2wsruW7sYL371FNFpsDgCcaGHJPr3o2aX+OgrgxHl0NwLAyd4Zj3066YkgROSlklpbxWSplq/1xt/36JlPI6+5+LpJTj7R+jpZSPX+71mklk3gRtdaYv6pseH0pqbAgfHHJUArfcuCiHmrvrgNGCSLJEd1/wbKNvgrN7oeaU6kiUmpcRS4Cvhd2lnQN/s/YmKFhv331qHfj7aQOi9/9qnmd4FgToaVSApeMS2H2yeuBFfSsLjB2oelqEVYfPkRAewISkCNWhaAOhp1GBT6ZRd5d2DXw3asF66Gg2/XVCSsnmvHI6nFUkuY90Aqd5Hh8/o8isnkbl+nGDkZKB13o68jYgjDtrE6tr7mBrvp4+9Qrd06j6Ro/rxw2mvl2ye6BFfXPeheAYGDbTMYF5qMNn6/jC87v5sMQBo5oDoBM4zTONvgna6uH4ZtWRKDUyNoSM+FBWDGQaVUo4/KZRvDcswXHBeaA1Oedo77Jx4wRznwevMfpmKNmnp1EzYvGzwMqBXCda6yF/jXFOTT59+sHBEnytgklxTivk0Sc6gdM8U8ocCIjQd9fADeMT2HuqhpLalit7g3MHjeK9Y29zbGAe6L0DJaREB+vdp96iu6ivya8TQX4+jIuxsnogRX3zVhm7T8fe7tjgPIzNJllx6Bxz0mII9lU7Sq8TOM0z9dyN2nGFiYuXuH6s0erpiqdRD78JFl8YZe7p07L6Vj4squLG8Ql6+tRbDEqGIZPgyFuqI1Fu2mAfKhvb2Hm88sre4PCbEDHU9L1P956u4VxdKzeMVz9KrxM4zXONvR3aGyBvtepIlEqODmbMkLAr241qs8GRd2DkfAiKdHxwHmTFoXNIiZ4+9TZj74DSw0adQxMbH2Ml1N+H5ftL+v/ixgpjucqY28DkNzfvHThLgK+Fa0fFqQ5FJ3CaB0ueBaGDjTtDk1s6LoGDZ2o5XdXcvxee3gkNJXr6FHj/wFnGDAljREyI6lA0RxpzCwgrHH5DdSRK+VkFS8bGszanlNaOrv69+OhykF2mnz5t77Sx4tA5FmbGE+Kvdv0b6ARO82QWK4y51dja3mzuUoDdw/nLD5zt3wsPvwm+QZC+xAlReY4TlU0cLK5j2fghqkPRHC0k1ig9dOhNY8TZxG6aMITGtk42HCvr3wsPvwmxoyEu0zmBeYit+RXUNndw00T3GKXXCZzm2cbdCbYO0y9SHhIRyPThkby7/yyyry1zOtuNGlkZ14NfsHMDdHMfHCxBCFg6frDqUDRnGHcn1J2GM7tUR6LUtOFRxIX5928ateakcd70KD3vHjhLZLAfs1JjVIcC6ARO83TxYyEmQ0+jArdMTOREZRMHztT27QXHN0FLjemnRaSULD9wlqnJkQwOD1QdjuYMGdcbI80mn0a1WgQ3jk9gS345tc3tfXvRkbeNz2NudV5gHqChtYMNR8tYOm4wvlb3SJ3cIwpNu1JCGAnI6Q9NX+tp8dh4/H0sLN/fx2nUI29B4CAYPte5gbm5nJJ6iiqaWDZBT596Lf8QSL/OGKnv7GPi4qWWTRhCR5dkZV93rR9+C5Kmw6Bhzg3Mza05Ukpbp42bJrrPdUIncJrn6x5BMvkoXFiAL/Mz4/jg0Dk6ui691sfS1WqUYMm8ySjJYmLvHyzBxyJ071NvN+4OY8S5cIPqSJQanRDGyNiQvt3oleUYLfb09CnvHShhWFQQE92oxZ5O4DTPN2iY0YT90BtGVwETu2XiEKqb2tmSV3HJ58VU7DR6Go67w0WRuafOLhvL958lKz2GQcHmTmS93oh5EBRl+mlUIQQ3TUhg98kaimsus2v90Otg8fmkr6xJldW3suN4JcsmDHGrGpE6gdO8w7g7oDIPSg+pjkSp2WkxRAb78e5l7q7jSzfBoBQj8TWxbYWVlDe0cdukJNWhaM5m9YXRtxh1I1vrVUejVPdygfcOXGIzQ1cnHHwdUhdCiHss2lflg4MlSAk3uVmNSJ3Aad4h8yajm8Ahc99d+1ot3DBuMOuPlVHX0tH7k2pPM6j2MEy4x/RFOd/aW8ygIF/mZcSqDkVzhXF3GO2gjr2vOhKlkiKDmDxs0KV3rRdthsZS4zphcu/sO8u4xHCGu1mNSJ3Aad4hKBLSFhkJXNdFEheTuPmqRNo7bay+2CLlg68Zn8ff5bqg3FBdcwfrj5axbMIQ/Hz0pdAUEqdA1EjY/7LqSJS7bVIiheWNF9+1fuBlCIyE1EUujcvdHDlbx9Fz9dw2KVF1KJ+hr1qa95h4LzSVG4V9TWx8YjjDo4N5p7dpVCnhwMvURIwz+hqa2AeHSmjvtLnlhVlzEiFgwueMDiRVx1VHo9T14wYT4Gvhzb3Fn32wpcbY5DTuDtNvcnprbzF+Vgs3ukHv0wvpBE7zHiMXQEgc7H9JdSRKCSG45aohfHyimlNVTZ9+8PSHUHOS0nhzlw4B48KcER/K6IQw1aForjT+bhAWY4TJxEIDfLlu7GA+OFBCS/sFrbWOvA1d7aafPm3r7GL5gbMsHB1HRJD7JbI6gdO8h9XHmBbMXwMN/WwV42VunZSIRcAbe858+oEDr4BfCBUxV6sJzE0Uljdw4Ewtt01KdKtdZZoLhA02bvYOvAK2fvYE9TK3T0qioa2TNTkXLLc48ArEjYH4cWoCcxMbjpZT29zBHZPdc5OTTuA07zLhXqPp8qHXVUei1ODwQLLSY3lzTzGd3TXh2psgZzlk3oTNGqA0PtXe2nsWq0Xo4r1mNfFz0HDO6EZiYtNSIhkaGcSbe3pMo5bnwtm9epMTxg1wQngAM0dGqw6lVzqB07xLTBokTTOmUU1eE+7OKUmUN7SxJd9eE+7YCmhvMP20SJdN8u7+YrLSYogJ9VcdjqZC2hKjJpzJl1tYLILbJyWy83gVZ6rtNeEOvmLUfhtr7hqR5+pa2FpQwa2TErFa3DOR1Qmc5n0m3mvUhCveozoSpeZlxBId4s9ru+3TqPte1LXfgOy8csrq27h9st68YFo+fkaD+9yV0FSlOhqlbp2UiBDGmlC6OuDAq7r2G0bpEClx601OOoHTvM/om43G1fv/qzoSpXytFm6dNIRNueVUnTgEp3bApM+Dxdz/7V/ZdZqYUH+uHRWnOhRNpYn3gq3D9C34EiICuWZkNG/tLcZ2bKWxk3/S51WHpZSUkjf2nGH68EiGRQWrDueizH0l17yTf6iRxB15B9oaVUej1J2Tk+iySYo3PmEUOp7wOdUhKVVS28LmvHLumJyIr1Vf/kwtbjQkTIR9/zH9cos7JidxtraF2u1PQ3gSjJyvOiSlPiqq5lRVM7e7eYcWfQXTvNNVDxjrvUx+dz08JoSZySGkFL+PHLXU9NMir+8+gwTummLuGnia3aTPQ3kOnNmlOhKlFo6OY3xwNZGlO+Cq+8FiVR2SUi/tOkV4oC/XjxusOpRL0gmc5p2SpkLcWNj9nOnvrr81+ChhNHJ08C2qQ1Gqs8vGG3vOMDs1hqTIINXhaO5g7O3gHwa7n1UdiVL+PlZ+EPcxndLCuRG3qQ5HqfKGVtYeKeW2SYkE+Lp3IqsTOM07CQFTHoSyw1C8W3U0Sk2qfI9TxPPESferJO5K2XkVnKtr5e6pevRNs/MLNgr7Hn0PGitUR6NOZztTalaxyTaRV46auxXhG7vP0GmTfG6a+18ndAKneS99dw3luVjOfMjxpFtZfbSc0rpW1REp8+rHp4kN9efaUbpxvdbDlAeNrgNm3vSUuwJrSyU5g2/ltd1naO+0qY5IiS6b5JVdp5k5MsrtGtf3RkkCJ4SIFEKsF0IU2D8P6uU56UKIAz0+6oUQ37I/9jMhxNkej13n8r+E5v78Q4y765x3oalSdTRq7HkOLL6kLXwUm5S88vFp1REpcaa6mc155dw5JUlvXtA+LSYdkmfB3ufN25lhz78hfCgTsm6hoqGNdUdLVUekxKbcckrqWrl32jDVofSJqivZY8BGKWUqsNH+9adIKfOklBOklBOASUAz8G6Pp/y5+3Ep5SpXBK15IDPfXbfWGS1xxtxKYtJQ5qbH8squ06a8u/7vR6cQQnCPB0yLaApMeRBqT0PhBtWRuF5ZDpzcBlO+yOyMeJIiA3npo1Oqo1LipY9OERvqz/xMzygxpCqBWwa8aP/zi8BNl3n+tcBxKaU5f6q0K9d9d73n3+a7u97/MrQ3wrQvAXDfjGFUNraxJsdcd9fN7Z289vFployJZ3B4oOpwNHeUsRRC4oxNT2az60nwCYSrHsBqEdwzdRgfFVVTUNagOjKXOlXVxNaCCu6aOtRjRulVRRknpTwHYP98uUUpdwGvXvC9rwkhDgkh/t3bFKymnTflIePuumC96khcx9YFHz9ltBUbchUAc1JjGBYVxH92nlQbm4u9ve8s9a2dfGFmsupQNHdl9TVKDxWsg+oi1dG4TlMVHHoDxt8JQZEA3DE5ET+rhf98aK7xkud3nMTHIjxi80I3IZ1UYkEIsQGI7+WhHwEvSikjejy3RkrZaxImhPADSoDRUsoy+/figEpAAr8EBkspv3iR1z8CPAIQFxc36bXXXrviv1NfNDY2EhLi/osfPclAz6mwdTL9o0doDhrCwQm/dGBk7iuqcjdjj/yKnMzvUBE76/z315zo4LW8dr4/QTIq3vt/TqWU/HB7CwFWwU9mBCCc1Jxb/793PFefU7+2KqZ/9AglCYsoTH3EZcd1ld7O59BTbzH8xH/ZPflvNIV8su7rucNt7Crt5E9zggjxc88+oI7U1CH5dnYzk+J8eGRc3/sju+JndO7cuXullJN7fVBK6fIPIA8j6QIYDORd4rnLgHWXeDwZONKX406aNEk62+bNm51+DLNxyDnd9mcpfxomZcnBgb+XJ3jxRin/kCFlZ/unvl3b1C5H/d9qeddfVysKzLW25JXLYd9fId/ee8apx9H/7x1PyTl9+xEpfzVYyuZq1x/byT5zPjvbpfzjKClfuOEzzz12rk4O+/4K+Y9NBa4JTrGnthTKYd9fIQ8X1/brda74GQX2yIvkNKqmUN8HHrD/+QHgvUs8924umD4VQvQsj3wzcMSh0WneZ9LnwS8EPvyH6kicrzwXirKNhdlW3089FB7ky11ThvLxuS5KalvUxOdCL+w8SXSIv9tXVNfcxNVfg44m2PuC6kic79gHUH8Wpn/5Mw9lxIcxKzWaF3ee9PpNT51dNl7YcZLpwyMZMyRcdTj9oiqB+w2wQAhRACywf40QIkEIcX5HqRAiyP74Oxe8/ndCiMNCiEPAXOB/XBO25rECI2DifXDkbag7qzoa5/rw7+ATcNGG1F+8JhkJPL/jhEvDcrWCsgY25ZbzuWlD8fdx74rqmpuIHwspc2DXU9DZrjoa55ESPvwnDEqB1IW9PuXhWcMpb2jj/YMlLg7OtVYfKaWkrpWHrhmuOpR+U5LASSmrpJTXSilT7Z+r7d8vkVJe1+N5zVLKKCll3QWvv09KOVZKOU5KeaO0b4jQtEua/ihIm7G431vVnYWDrxvJanB0r09JHBTE1Hgrr358hvpW7626/uSWIgJ9rTxwdbLqUDRPcvXXoeEc5Fw4buBFTm6Hs3uMEceL9D2dlRpNelwoz24r6l6u5HWklDy7/QQp0cHMy/C8At+esVdW0xxhUDKMuhH2vABtXrpF/sN/Gknq1V+/5NMWJ/vS2NbJq7u8s7Dv2doW3jtwlrumJhEZ7Kc6HM2TjJwPMRmw8x/e20d5+58gOBYm3HvRpwgheHBWCrmlDWwv9M5C6B+fqObgmVq+ODMZi8XzNmvoBE4zl6u/Dm113rnGpbna+HuNvQ0GXbqSeHK4latHRPH8Du9c4/LMVqMUxEOzPG9aRFNMCJjxNaOPcuFG1dE4Xsl+OL4JZnwFfAMu+dRlExKICfXniezjLgrOtf6xuZDoED9un5ykOpQrohM4zVwSJ0PKbNjxN2hvVh2NY338jLEAe+Y3+/T0R2YPp7S+lXf3Fzs5MNeqbmrntd2nWTZhCEMidOFe7QqMuxPCk2DLb7xvFG77X4we0ZN7rbz1Kf4+Vr40ezg7j1ex+2S182NzoYNnatlWUMmD1wwnwNcz18jqBE4znzmPQVM57Hvx8s/1FO1NRkX1tMUQN7pPL5mTFsO4xHD+sbmQji7vGYV7YccJWjtsfDlLj75pV8jHD675FhTvNnZ0e4vKQjj6nlHcPKBvOy4/N20Y0SF+/G1jgZODc61/bi4kPNCXe6d7TuHeC+kETjOf5Jkw7BrjTrSjVXU0jrHneWiphmv6viFbCMG35qdyprqFd/d5x87cupYOXth5kgWZcYyMDVUdjubJJt4HoQmw9feqI3GcHX8GH/9eS4dcTKCflYdmDWdbQSX7T9c4MTjXyS2tZ93RMj5/dTKhAb6Xf4Gb0gmcZk5Z34fGUtj3H9WRDFxbo7EoeXgWDJ3er5fOTY9lXGI4f99c4BWjcM9tP0F9ayffvDZVdSiap/PxN0bhTu0wdm16uMDmEjjwqlFeKKR/Oy7vmz6MQUG+/H1ToXOCc7F/bCok2M/q8e31dAKnmVPyLBg6A7b/GTrbVEczMB8/Bc1VMPfH/X6pN43C1TS18+/tJ1gyJt7jCnJqbuqq+40m99m/UR3JgCWffNWelH67368N9vfhoVnD2ZRbzuHiusu/wI3llNSx4tA5Pj8zmYggz96hrhM4zZyEgDnfh4YSz96R2lILO/5qrH1LmnJFb+Eto3BPbS2iqb2T/1mQpjoUzVv4Bhqbgk5ug6ItqqO5cmVHiS3fBlMfgdC4K3qL+2cMIzzQlz+sy3NwcK71x3X5hAf68sjsEapDGTCdwGnmNTzLGInb8ltorVcdzZX56F/QWgdzf3jFb9FzFO613WccGJzrVDS08eLOk9w4PoG0OL32TXOgyQ9CWCKs/wnYPPQGJ/v/0WUN7PMO9d6EBvjy1bkj2JJfwU4PrQu352Q1m3LLeXTOCMIDPXftWzcf1QGo1tHRQXFxMa2tjlnMHh4ezrFjxxzyXlciICCAxMREfH09/4fT6YSABb+AZ+bCzr/BvP5PQSrVUGYU7h11IwweP6C3mpsey9SUSP6yPp+bJiR43MLev28qoL3Lpte+aY7nGwDzfgTLvwxH34Uxt6qOqH+K98KxDziTfDcpQZEDeqv7ZyTzwo6T/GZNLsu/MtOjit9KKfndmjxiQv35vJd0ZzF9AldcXExoaCjJyckIMfAfxoaGBkJD1YwASCmpqqqiuLiYlJQUJTF4nCFXGRfkD/9pv9P2oKbnm39lrN+b/7MBv5UQgh9dN4pl/9zBU1uK+M6i9IHH5yIFZQ28vOs090wdyvCYENXhaN5o3J1GZ4aNv4CMG4wyI55ASlj7AwiOpTjxRgb6WyHA18q3F6bznTcPsurIOZaOS3BImK6wKbecj09W88tlown088y6bxcy/RRqa2srUVFRDkneVBNCEBUV5bDRRNOY93/Q1QHZv1YdSd+VHoZ9/zXWtEQ5Zi3H+KQIlk1I4JltRZyra3HIe7rCr1YeI8jPqte+ac5jscKCn0PNSdjzb9XR9F3OO3BmF1z7f3T5BDnkLW+eOISM+FB+vzaPts4uh7yns7V1dvHLFUcZERPMXVM9t+7bhUyfwAFekbx186a/i8tEpsDUh2H/f6HkgOpoLk9KWPtDCBwEc77r0Lf+zsJ0pITfr/WMhcrZeeVsya/gG/NSdc9TzblGzoeUOZD9/6CxQnU0l9fRAut/CvFjYcLnHPa2VovgB9eN4lRVM89uO+Gw93WmF3ac5GRVMz+5YTS+Vu9Je7znb+JlHnroIY4ePao6DPOY830IioaV/+v+C5XzVsGJrZD1AyOJc6CkyCAempXCO/vOsquoyqHv7WgdXTYeX3mMYVFB3H/1pXu/atqACQHX/d7oerLhZ6qjubwP/wF1Z2DRr40RRAeakxbDotFx/H1TAWdr3Xu0vryhlb9vKmT+qFjmpMWoDsehdALnpp599lkyMzNVh2EegRGw8Jdwdo8xEueu2hpg1fcgNhMmf8Eph/j6vFSGRATy4+VH3LrR/dNbiygob+TH12fi7+Mda1o0NxeTDjO+CgdegtO7VEdzcdVFsPUPMOoGSJnllEP831Lj99OvVrj3QMNvVxtTvT+63vt+n+oEzg00NTVx/fXXM378eMaMGcPrr79OVlYWe/bsASAkJIQf/ehHjB8/nunTp1NWVqY4Yi817k4YerVxd93spo2bNz0O9Wfhhr+C1Tk7RQP9rPxi2WgKyht5brt7TpGcqGzirxsLWDImngWZV1bXStOuyOzvGS22Vv0vdHWqjuazpIQPvgUWX1jyO6cdJnFQEF+fl8rqI6VsyXfPKeXtBZW8va+Yh2cNJyU6WHU4Dmf6Xag9/fyDHI6WDKweWFdXF1brJ6MBmQlh/PSGSzcXX7NmDQkJCaxcuRKAuro6nnjiifOPNzU1MX36dB5//HG+973v8cwzz/DjH3tYyQtPIARc/0d48hpY8xjc8rTqiD6teK/RsH7KQ5A01amHunZUHItGx/HXjfksHTeYpEjHLIB2BCklP3r3MP5WCz+78dL/tzTN4fxDYPGv4c0HYOdfYdb/qo7o0w6+Cie2wHV/gDDn7hJ9aFYKb+8r5ofvHGbNt2a5Vfmh5vZOfvDuIVKig/mGl5YX0iNwbmDs2LFs2LCB73//+2zbto3w8E+3AfLz82Pp0qUATJo0iZMnTyqI0iTiMmH2d+DQ63D0fdXRfKKzHT74BoTGw7U/cckhf3rDaHwsFv73zYPYbNIlx+yLN/cWs/N4Fd9fkkFcWIDqcDQzylxmfGz+NZTlqI7mE40VxganpGlGWSQn8/ex8vvbxnOuroXHV6qrf9qbP63L50x1C7+5ZSwBvt65xEKPwPVwuZGyvriSOnBpaWns3buXVatW8YMf/ICFCxd+6nFfX9/zu0utViudnW44bO9NZn8X8tfAiv8x+qWGuMHC182/grIjcNerEBDmkkMmRATy0xsy+e5bh/j3jhM8NGu4S457KaermvnFB0eZmhzJPV5UDkDzMELA9X+CUzvh3Ufh4U1OW9LQZ1LC+1+D9mZjiYXFNeMzk4YN4uHZw3lqSxGLxsQzNz3WJce9lJ3HK3luxwk+N20o04ZHqQ7HafQInBsoKSkhKCiIe++9l+985zvs27dPdUjmZvWFm58yNgys+JZxYVTpxFbY8TeY9AXIuM6lh75tUiILMuP43do88kobXHrsC3V22fjm6/sRAv5053iPqgKveaHgaFj6Fyg9ZLTjU233s8aN54JfQOwolx76f+ankRYXwmNvH6K6qd2lx75QTVM73379IClRwfzoeteeB1fTCZwbOHz4MFOnTmXChAk8/vjjen2bO4gdZUxV5q4w1p2p0lRp3OFHjYRFj7v88EIIfn3LWMICfPnyy3tpbFM3+vvXjQXsP13L4zePJXGQ+6zJ00xs1FKjxtrWP0DhBnVxlOXAuh/DyAUw7UsuP3yAr5U/3TGBmqYOvvX6AboULbmQUvLYO4eoamrjb3dPJMjPuycZdQLnBhYtWsShQ4c4cOAAu3fvZvLkyWRnZzN58mQAGhsbzz/3tttu44UXXlAUqcnM+CpkLDUujKc/cv3xuzrgzc9DcxXc+iz4qdlFFR3izz/umcipqma+99ZBpIIRybU5pfx9UyG3TUrkxvGe075HM4Hr/mCU9Xn7Yag94/rjN1fDa/dAQDjc9C9jeleBMUPC+emNmWzNr+DvmwqUxPDEluOszSnj+4szGDMk/PIv8HA6gdO0ixHCuCBGDIU3HoC6s649/rr/g5PbjPUsCRNce+wLTB8exfcWpbPqcClPbily6bELyhr49usHGJ8Yzq9uGuPSY2vaZfkFwR3/MW64Xr/XKPTrKl2d8NYXob4E7nwJQtSuP7tn6lBumTiEv24sYF1OqUuPvSm3jN+vzePG8Qk8eI05eoHrBE7TLiUg3LgwtjfBy7dBS61rjvvxM7DrCZj+FRh/l2uOeRmPzB7O0nGD+e2aXN474Jpktry+lQdf3EOgn5Un75vktbvJNA8XPdIYJS89ZCRUrqgPJyWs/h4UbTY2VDi5tFBfCCF4/OaxjEuM4Buv7Wf/6RqXHDenpI5vvnqAzMFh/PbWcaZpKakTOE27nLjRcNdLUFkAr30OOlqde7xDb8Kq70D69bDgl849Vj8IIfjjHeOZlhLJd948yPaCSqcer7a5nfue+5jKxjaefWAKg8MDnXo8TRuQ9MVGHcn8NbDyf5zfkm/TL2HPczDzm3DVfc49Vj8E+ll57oHJxIYG8NCLezhe0Xj5Fw1AUUUj9z/3MaEBPjxz/2QC/cxzk6cTOE3ri+FZcNMTcGoHvHKH86ZJcpbD8kcheRbc9m+wutciXH8fK0/fP5nh0SE8+OJup1Vgr21u54Hnd3Oisoln7p/MhKQIpxxH0xxq8hdh1ndg339gxTedk8RJCVt/D9v+CJM+D/N/7vhjDFB0iD8vfGEKAHc+9RH5Zc7ZwX6ysol7nzVamr300DQSIsx1k6cTOE3rq3G3G+VFTm6D/94CLQ6eHtj9nLFpYchkuOsV8HXPIrXhgb688vA0RsSE8PCLe1hz5JxD37+ktoXbnvyQYyX1/OOeicwcGe3Q99c0p5r3Y6OW5L7/GDdjnW2Oe2+bzegSs+lXRuu/6/+kbNPC5QyPCeH1L03HIuCupz/iUHGtQ9//UHEttz6xk5aOLl784lSGx4Q49P09gU7gNK0/xt8Jt78AZ/fC01lQemTg79nVAWt/BCu/DWmL4L53XVas90pFhfjz6sPTyUwI49GX9vHn9fkO6daw91QNt/xrJ2V1rbz4xaksHB3vgGg1zYWEMJK4ef9ndHR5YSnUO+Amp7UO3rzfKGs0/atw05Ngce/pwpGxobz+pRkE+lq5/ckPeWdfsUPed/Xhc9z19EcE+ll568tXm2LHaW90Aqdp/ZW5DL6wyrizfna+seHgSqdKKgvghevhw38YPU7vfMnY1eYBwoN8ee2R6dxylbHr7PMv7OZsbcsVvVdHl41/ZRdy51Mf4usjeP1LM5gxwnsrqGsmMPs7xs1eWQ48PQdyV135e53+CJ6abbzHov9n1IR0UaeFgUqJDub9r81k4tAIvv3GQb7/1iHqWzuu6L0aWjv48fLDfPnlfaTFhfLOl69mhAlH3rop+QkQQtwuhMgRQtiEEJMv8bzFQog8IUShEOKxHt+PFEKsF0IU2D8Pck3kmmaXNBUe2QJDpxkbDv69EE5s6/vrm6thw8/hiauhPBdufc5YAK26HU8/Bfha+ePt4/nlTWPYfaKahX/awj83F/a54K+Uks255Sz923Z+tyaPBZlxrPj6LDIT3HsEUtP6ZPTN8NAGCIqG1+42NkGV96NnaM1JWP4V+PcisHXBF1Yb9SnddNr0YqJC/HnpwWk8OmcEb+49w4I/beG1j0/T0dW3G9+OLhtv7S3m2j9u4eVdp3l4VgpvfGkGsSbvhaxqhfQR4BbgqYs9QQhhBf4JLACKgd1CiPellEeBx4CNUsrf2BO7x4DvOz9s5/jPf/7DH/7wB4QQjBs3jl/96ld88YtfpKKigpiYGJ5//nmGDh3Km2++yc9//nOsVivh4eFs3bpVdejmFhoH9y2Hg6/Bhp/Ci0uN9Wvj74KR82FQ8qcvtG2NUPwx5LwLh9+GjiYYe4dxN624ftNACCG4b/owstJi+PkHR/n92jye3lrEsgkJXD92MOOTIj5V/sNmk5ysamJTbjlv7S0mt7SBIRGBPH3fJD1lqnmfuEx4JBt2/g22/wVyV8LIa401bCmzIfSCn/nmamOd7ZG34dgKEBZjp+mc7ysr5u0IPlYLjy3J4Lqx8fzfezk89s5h/rqxgFuuGsKi0fFkDg7Dx/rJmFJnl43c0gbWHS3j7b3FnK1tYcyQMJ66bxITh+oxG1CUwEkpjwGXq9UyFSiUUhbZn/sasAw4av+cZX/ei0A2jkjgVj8GpYcH9BaBXZ2f3jkYPxaW/Oaiz8/JyeHxxx9nx44dREdHU11dzQMPPMD999/PAw88wL///W++8Y1vsHz5cn7xi1+wdu1ahgwZQm1t7YDi1BxECJhwN4y+yVi0vPcFY0QOICDCuDhb/aC11l6lXYJfiDENO/MbLu9Z6ExJkUE8+8BkDp6p5ZltRby++wz/+fAUPhZBQkQg4YG+tHR0UVbXSoN9hG7skHB+d9s4bp44BF+rZ0wJaVq/+fgZU6qTv2isYTvwCrzzsPFYcCyExBl/bq6ChhLjz0HRMP3LxohbmPd0HxmXGMHyr1zN5rxyXth5iieyj/PPzccJ8LUwODyQEH8fmto7OVvTQlunDYswCon/Ytlo5mXEmqbGW18IFW1xzh9ciGzgO1LKPb08dhuwWEr5kP3r+4BpUsqvCSFqpZQRPZ5bI6XsNSUXQjwCPAIQFxc36bXXXvvU4+Hh4YwcORIA/80/xVKeM7C/lAR6/HzZYkfTNvfi27yffPJJysvL+clPfnL+e8nJyRQUFODr60tHRwepqamcPHmSb33rW5w4cYKbb76ZG264gaio3tcIFRYWUldXN7C/hxtpbGwkJMRz1jkENZ0mojaHkMYT+HbUY7F10OkTTEvgYOrDUqmNGIvN6q80Rlec0+YOSV5NF8drbVS12GjqBD8LhPkLhoVZyBhkJS7YO5I2T/sZ9QRefU6ljdCGQsLrjhHcdBrfjnpA0OkTRFPwUOrD0qgPG4V04CYFdz2ftW028qptFNV1UdMqae0Efx+IDBAMC7MyOspKuL97Jm2uOKdz587dK6XsdamZ00bghBAbgN7mQ34kpXyvL2/Ry/f6nW1KKZ8GngaYPHmyzMrK+tTjx44dIzQ01Pji/7d3fzFS3WUYx78PC+zYdg0a0BSG2LUhtWVTutqUSkGSbhsRG6gXTWqrroF4o63VKErDHYmGZLVRtGoaqG3ipgYRIhb7h5RuTEwl1bq2INUtVmFbLOuQthsJrYTXiznUBabNLpyd356zzyfZzJwzw5xnXmZn3v2dM+e34p6xPvxZhoeH//94menvcP/W1lZaW1tP+zeSaGtre6uBmzJlCm1tbWzevJk9e/awc+dOlixZQn9/f8MmrlKp0NnZed7PZaLo6+vjzP83Oz/Nqunycd/CxODXaP7KX9Prm7q18tez+VLXdNz+/I2IGyKio8HPaJo3qB/3NnfEchXIxpZ5RdLFANnlkfySN1dXVxdbtmyhVqsBcPToURYtWsSpkcLe3l4WL14MwIEDB1i4cCHr169n5syZHDqUYOJkMzMzS25ineb9dE8D8yS1Ay8BtwK3ZbftALqBDdnlaJvCCWf+/PmsW7eOpUuX0tLSQmdnJxs3bmTVqlX09PS89SUGgDVr1jAwMEBE0NXVxYIFCxKnNzMzsxSSNHCSPgX8AJgF7JTUHxEflzQb2BQRyyPihKQ7gMeAFuD+iDh1gNoGYIuk1cBB4JYETyM33d3ddHd3n7Zu9+7dZ91v27ZtzYpkZmZmE1iqb6FuB7Y3WP8yIw6biYjfAGed/TAiakDXeGY0MzMzm6jK8RUwMzMzs0nEDZyZmZlZwbiBoz6dT1mU6bmYmZlZY5O+gatUKtRqtVI0PhFBrVajUpnc88OZmZmV3UQ+jUhTVKtVBgcHGRoayuXxjh8/nrSBqlQqVKvVZNs3MzOz8TfpG7hp06bR3t6e2+P19fWVahYEMzMzm3gm/S5UMzMzs6JxA2dmZmZWMG7gzMzMzApGZfj25WhJGgL+Oc6bmQn8e5y3Mdm4pvlzTfPleubPNc2X65m/ZtT0AxExq9ENk6qBawZJf4iIq1PnKBPXNH+uab5cz/y5pvlyPfOXuqbehWpmZmZWMG7gzMzMzArGDVz+7ksdoIRc0/y5pvlyPfPnmubL9cxf0pr6GDgzMzOzgvEInJmZmVnBuIHLkaRlkv4q6QVJa1PnKTJJcyU9KWm/pH2S7kqdqSwktUj6k6SHU2cpA0kzJG2V9Hz2ev1o6kxFJumr2e/8XkkPSUo3uXRBSbpf0hFJe0ese6+kXZIGssv3pMxYNG9T057s9/5ZSdslzWhmJjdwOZHUAtwLfAK4Avi0pCvSpiq0E8DXIuJy4FrgS65nbu4C9qcOUSLfBx6NiA8BC3Btz5mkOcCXgasjogNoAW5Nm6qQHgCWnbFuLfBERMwDnsiWbfQe4Oya7gI6IuJK4G/A3c0M5AYuP9cAL0TE3yPiTeDnwMrEmQorIg5HxDPZ9WHqH4pz0qYqPklV4JPAptRZykDSu4GPAZsBIuLNiHg1aajimwq8S9JU4ALg5cR5CicifgscPWP1SuDB7PqDwM3NzFR0jWoaEY9HxIls8fdAtZmZ3MDlZw5waMTyIG44ciHpEqAT2JM4Shl8D/gGcDJxjrL4IDAE/DTbLb1J0oWpQxVVRLwEfAc4CBwGXouIx9OmKo33R8RhqP+BDLwvcZ6yWQU80swNuoHLjxqs81d8z5Oki4BfAl+JiNdT5ykySTcBRyLij6mzlMhU4MPAjyOiE/gP3jV1zrLjslYC7cBs4EJJn0mbyuydSVpH/bCf3mZu1w1cfgaBuSOWq3jo/7xImka9eeuNiG2p85TAdcAKSf+gvov/ekk/Sxup8AaBwYg4NTq8lXpDZ+fmBuDFiBiKiP8C24BFiTOVxSuSLgbILo8kzlMKkrqBm4Dbo8nnZXMDl5+ngXmS2iVNp37g7Y7EmQpLkqgfV7Q/Iu5JnacMIuLuiKhGxCXUX5+7I8KjG+chIv4FHJJ0WbaqC/hLwkhFdxC4VtIF2XtAF/5SSF52AN3Z9W7gVwmzlIKkZcA3gRURcazZ23cDl5PsQMY7gMeov+FsiYh9aVMV2nXAZ6mPEvVnP8tThzJr4E6gV9KzwFXAt9PGKa5sJHMr8AzwHPXPKM8gMEaSHgKeAi6TNChpNbABuFHSAHBjtmyj9DY1/SHQBuzKPqN+0tRMnonBzMzMrFg8AmdmZmZWMG7gzMzMzArGDZyZmZlZwbiBMzMzMysYN3BmZmZmBeMGzsysAUkzJH0xuz5b0tbUmczMTvFpRMzMGsjm4H04IjpSZzEzO9PU1AHMzCaoDcClkvqBAeDyiOiQ9HngZqAF6AC+C0ynfuLpN4DlEXFU0qXAvcAs4BjwhYh4vtlPwszKybtQzcwaWwsciIirgDVn3NYB3AZcA3wLOJZNZv8U8LnsPvcBd0bER4CvAz9qRmgzmxw8AmdmNnZPRsQwMCzpNeDX2frngCslXUR9EvZf1Kf0BKC1+THNrKzcwJmZjd0bI66fHLF8kvr76hTg1Wz0zswsd96FambW2DD1iarHLCJeB16UdAuA6hbkGc7MJjc3cGZmDUREDfidpL1Azzk8xO3Aakl/BvYBK/PMZ2aTm08jYmZmZlYwHoEzMzMzKxg3cGZmZmYF4wbOzMzMrGDcwJmZmZkVjBs4MzMzs4JxA2dmZmZWMG7gzMzMzArGDZyZmZlZwfwPWx0cGu7Xp7gAAAAASUVORK5CYII=",
      "text/plain": [
       "<Figure size 720x432 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.figure(figsize=(10,6))\n",
    "plt.plot(t, np.sin(t), label = 'sin')\n",
    "plt.plot(t, np.cos(t), label = 'cos')\n",
    "plt.grid(True) #격자무늬\n",
    "# plt.legend(labels=['sin','cos']) #범례 이렇게도 가능\n",
    "plt.legend(loc = 'lower left') \n",
    "plt.title('Example of sinewave')\n",
    "plt.xlabel('time')\n",
    "plt.ylabel('amlitude') #진폭\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 193,
   "metadata": {},
   "outputs": [],
   "source": [
    "def drawGraph():\n",
    "    \n",
    "    plt.figure(figsize=(10,6))\n",
    "    plt.plot(t, np.sin(t), label = 'sin')\n",
    "    plt.plot(t, np.cos(t), label = 'cos')\n",
    "    plt.grid(True) #격자무늬\n",
    "    # plt.legend(labels=['sin','cos']) #범례 이렇게도 가능\n",
    "    plt.legend(loc = 'lower left') \n",
    "    plt.title('Example of sinewave')\n",
    "    plt.xlabel('time')\n",
    "    plt.ylabel('Amplitude') #진폭\n",
    "    plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 194,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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",
      "text/plain": [
       "<Figure size 720x432 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "drawGraph()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 예제2: 그래프 커스텀"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 195,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([0. , 0.5, 1. , 1.5, 2. , 2.5, 3. , 3.5, 4. , 4.5])"
      ]
     },
     "execution_count": 195,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "t = np.arange(0, 5, 0.5)\n",
    "t"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 198,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<function matplotlib.pyplot.show(close=None, block=None)>"
      ]
     },
     "execution_count": 198,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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1UtjM8al8B5gwdm9O9m1q7vcfXf388gjk1WrurF//MfJY3ffnfzkTyaPeES/KxeggLnhMH9YJGrtNjFLkv/6r+SHP5wcUI44IjnzzG78M59J7rhjcog56aTkl36pG//d30127JgY27Urecxjkle9qht/whOS731vckj65V9O/uAPujoOO2x6fa94RfK2tyU/+lHycz83ffz1rxeg4FAztHMoF37kwnzo2R/KmiPtwAiHjFqTe+6ZCBrHHtuFmO9+t2tv9gaU3buT88/vHve5zyVf+9rkgLJ8efKGN3Tjb397snHj5IBy7LHJX/91N37RRcn1109+/oc+NPnyl7vxpz41+eIXJ9d6zjnJhg3d7694RfL1r08eP/fciQB19dXJ7bcnK1cmK1Z0l5NPnrjvsccm97//xNjKlRPhp5TkjW/sQtT42IoVE+HtPvdJrrtu8tjKld1zLgACFBxEA+sHsuHWDRm4YSCXP+3yfpcDS9/oaNfJ6A0Q412U+943GRpKvvrVyWN3350885nJAx+YbN6cfPzj06eZ3vKWbprp6quTK66YPs30T/+UHHNM8v/+X/KmN3W39frRj7ow8OY3J3/8x5PHli3rQlSSvP/9yeDgxFgp3bz4eIC6+eYuDPUGlN6uzllnJYcfPjmEPOhBE+Ove13y3/89OaCsWjUx/rd/24W/3scfccTE+NRwNdV4kNuT3/7tPY8tW5Y88Yl7f3wflVrrQXuxtWvX1s2bNx+014OFZGjnUE59x6m5e/fdOWL5EbnlsluWVBdqfEZgJgfxnxkWglq74LJsWTIyknznO9MDyskndyHmBz9IPvGJ6QHl3HOTs89Obr01eetbpweUV74yWbeuCzgvfOHksV27kr/8y+Tnfz752MeSCy6YXuPnP989/gMfSJ73vOnjmzcnj3pU8u53Jy96URdCerssN9yQnHpq9/h3vWvy2MqV3W1HH5383d91HaDesRUrkksu6Z7zK19JvvWtyWMrVnRdmlKSO+/swtT42PLle/+fjTlVSrmx1rp2pjEdKDhIek+2O36SXV0o5kytEwty7767+5J94AO7sa9+NbnrrskhZvXq5LGP7cavuKILMr3jj3xkcuGF3fiv/Mr0Ls6zn91N7/zP/yRnnDF5bHg4+Z3f6bovd9wxeUpn3FvekrzmNd30z3OfO338qKO6APX97ycf/OD0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",
      "text/plain": [
       "<Figure size 720x432 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.figure(figsize=(10,6))\n",
    "plt.plot(t,t, \"r--\")\n",
    "plt.plot(t,t ** 2, \"bs\")\n",
    "plt.plot(t,t ** 3, \"g^\")\n",
    "plt.show"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 200,
   "metadata": {},
   "outputs": [],
   "source": [
    "#t = [0,1,2,3,4,5,6]\n",
    "t = list(range(0,7))\n",
    "y = [1,4,5,8,9,5,3]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 207,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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",
      "text/plain": [
       "<Figure size 720x432 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "def drawGraph():\n",
    "    plt.figure(figsize=(10,6))\n",
    "    plt.plot(\n",
    "        t,\n",
    "        y,\n",
    "        color='green',\n",
    "        linestyle='dashed',\n",
    "        marker='o',\n",
    "        markerfacecolor='blue',\n",
    "        markersize=15,\n",
    "    )\n",
    "\n",
    "    plt.xlim([-0.5, 6.5])\n",
    "    plt.ylim([0.5,9.5])\n",
    "    plt.show()\n",
    "    \n",
    "drawGraph()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 예제3: scatter plot"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 208,
   "metadata": {},
   "outputs": [],
   "source": [
    "t = np.array(range(0,10))\n",
    "y = np.array([9,8,7,9,8,3,2,4,3,4])\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 210,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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",
      "text/plain": [
       "<Figure size 720x432 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "def drawGraph():\n",
    "        \n",
    "    plt.figure(figsize=(10,6))\n",
    "    plt.scatter(t,y)\n",
    "    plt.show\n",
    "\n",
    "drawGraph()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 212,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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",
      "text/plain": [
       "<Figure size 1440x432 with 2 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "colormap = t\n",
    "\n",
    "def drawGraph():\n",
    "    \n",
    "    plt.figure(figsize=(20, 6))\n",
    "    plt.scatter(t, y, s=50, c=colormap, marker='>')\n",
    "    plt.colorbar()\n",
    "    plt.show()\n",
    "    \n",
    "drawGraph()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 예제4: pandas에서 plot그리기\n",
    "- matplotlib 을 가져와서 사용합니다"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 213,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>소계</th>\n",
       "      <th>최근증가율</th>\n",
       "      <th>인구수</th>\n",
       "      <th>한국인</th>\n",
       "      <th>외국인</th>\n",
       "      <th>고령자</th>\n",
       "      <th>외국인비율</th>\n",
       "      <th>고령자비율</th>\n",
       "      <th>CCTV비율</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>구별</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>강남구</th>\n",
       "      <td>3238</td>\n",
       "      <td>150.619195</td>\n",
       "      <td>561052</td>\n",
       "      <td>556164</td>\n",
       "      <td>4888</td>\n",
       "      <td>65060</td>\n",
       "      <td>0.871220</td>\n",
       "      <td>11.596073</td>\n",
       "      <td>0.577130</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>강동구</th>\n",
       "      <td>1010</td>\n",
       "      <td>166.490765</td>\n",
       "      <td>440359</td>\n",
       "      <td>436223</td>\n",
       "      <td>4136</td>\n",
       "      <td>56161</td>\n",
       "      <td>0.939234</td>\n",
       "      <td>12.753458</td>\n",
       "      <td>0.229358</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>강북구</th>\n",
       "      <td>831</td>\n",
       "      <td>125.203252</td>\n",
       "      <td>328002</td>\n",
       "      <td>324479</td>\n",
       "      <td>3523</td>\n",
       "      <td>56530</td>\n",
       "      <td>1.074079</td>\n",
       "      <td>17.234651</td>\n",
       "      <td>0.253352</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>강서구</th>\n",
       "      <td>911</td>\n",
       "      <td>134.793814</td>\n",
       "      <td>608255</td>\n",
       "      <td>601691</td>\n",
       "      <td>6564</td>\n",
       "      <td>76032</td>\n",
       "      <td>1.079153</td>\n",
       "      <td>12.500021</td>\n",
       "      <td>0.149773</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>관악구</th>\n",
       "      <td>2109</td>\n",
       "      <td>149.290780</td>\n",
       "      <td>520929</td>\n",
       "      <td>503297</td>\n",
       "      <td>17632</td>\n",
       "      <td>70046</td>\n",
       "      <td>3.384722</td>\n",
       "      <td>13.446362</td>\n",
       "      <td>0.404854</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "       소계       최근증가율     인구수     한국인    외국인    고령자     외국인비율      고령자비율  \\\n",
       "구별                                                                         \n",
       "강남구  3238  150.619195  561052  556164   4888  65060  0.871220  11.596073   \n",
       "강동구  1010  166.490765  440359  436223   4136  56161  0.939234  12.753458   \n",
       "강북구   831  125.203252  328002  324479   3523  56530  1.074079  17.234651   \n",
       "강서구   911  134.793814  608255  601691   6564  76032  1.079153  12.500021   \n",
       "관악구  2109  149.290780  520929  503297  17632  70046  3.384722  13.446362   \n",
       "\n",
       "       CCTV비율  \n",
       "구별             \n",
       "강남구  0.577130  \n",
       "강동구  0.229358  \n",
       "강북구  0.253352  \n",
       "강서구  0.149773  \n",
       "관악구  0.404854  "
      ]
     },
     "execution_count": 213,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data_result.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 214,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:xlabel='구별'>"
      ]
     },
     "execution_count": 214,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\jcc96\\anaconda3\\envs\\ds_study\\lib\\site-packages\\IPython\\core\\pylabtools.py:151: UserWarning: Glyph 44053 (\\N{HANGUL SYLLABLE GANG}) missing from current font.\n",
      "  fig.canvas.print_figure(bytes_io, **kw)\n",
      "C:\\Users\\jcc96\\anaconda3\\envs\\ds_study\\lib\\site-packages\\IPython\\core\\pylabtools.py:151: UserWarning: Glyph 45224 (\\N{HANGUL SYLLABLE NAM}) missing from current font.\n",
      "  fig.canvas.print_figure(bytes_io, **kw)\n",
      "C:\\Users\\jcc96\\anaconda3\\envs\\ds_study\\lib\\site-packages\\IPython\\core\\pylabtools.py:151: UserWarning: Glyph 44396 (\\N{HANGUL SYLLABLE GU}) missing from current font.\n",
      "  fig.canvas.print_figure(bytes_io, **kw)\n",
      "C:\\Users\\jcc96\\anaconda3\\envs\\ds_study\\lib\\site-packages\\IPython\\core\\pylabtools.py:151: UserWarning: Glyph 46041 (\\N{HANGUL SYLLABLE DONG}) missing from current font.\n",
      "  fig.canvas.print_figure(bytes_io, **kw)\n",
      "C:\\Users\\jcc96\\anaconda3\\envs\\ds_study\\lib\\site-packages\\IPython\\core\\pylabtools.py:151: UserWarning: Glyph 48513 (\\N{HANGUL SYLLABLE BUG}) missing from current font.\n",
      "  fig.canvas.print_figure(bytes_io, **kw)\n",
      "C:\\Users\\jcc96\\anaconda3\\envs\\ds_study\\lib\\site-packages\\IPython\\core\\pylabtools.py:151: UserWarning: Glyph 49436 (\\N{HANGUL SYLLABLE SEO}) missing from current font.\n",
      "  fig.canvas.print_figure(bytes_io, **kw)\n",
      "C:\\Users\\jcc96\\anaconda3\\envs\\ds_study\\lib\\site-packages\\IPython\\core\\pylabtools.py:151: UserWarning: Glyph 44288 (\\N{HANGUL SYLLABLE GWAN}) missing from current font.\n",
      "  fig.canvas.print_figure(bytes_io, **kw)\n",
      "C:\\Users\\jcc96\\anaconda3\\envs\\ds_study\\lib\\site-packages\\IPython\\core\\pylabtools.py:151: UserWarning: Glyph 50501 (\\N{HANGUL SYLLABLE AG}) missing from current font.\n",
      "  fig.canvas.print_figure(bytes_io, **kw)\n",
      "C:\\Users\\jcc96\\anaconda3\\envs\\ds_study\\lib\\site-packages\\IPython\\core\\pylabtools.py:151: UserWarning: Glyph 44305 (\\N{HANGUL SYLLABLE GWANG}) missing from current font.\n",
      "  fig.canvas.print_figure(bytes_io, **kw)\n",
      "C:\\Users\\jcc96\\anaconda3\\envs\\ds_study\\lib\\site-packages\\IPython\\core\\pylabtools.py:151: UserWarning: Glyph 51652 (\\N{HANGUL SYLLABLE JIN}) missing from current font.\n",
      "  fig.canvas.print_figure(bytes_io, **kw)\n",
      "C:\\Users\\jcc96\\anaconda3\\envs\\ds_study\\lib\\site-packages\\IPython\\core\\pylabtools.py:151: UserWarning: Glyph 47196 (\\N{HANGUL SYLLABLE RO}) missing from current font.\n",
      "  fig.canvas.print_figure(bytes_io, **kw)\n",
      "C:\\Users\\jcc96\\anaconda3\\envs\\ds_study\\lib\\site-packages\\IPython\\core\\pylabtools.py:151: UserWarning: Glyph 44552 (\\N{HANGUL SYLLABLE GEUM}) missing from current font.\n",
      "  fig.canvas.print_figure(bytes_io, **kw)\n",
      "C:\\Users\\jcc96\\anaconda3\\envs\\ds_study\\lib\\site-packages\\IPython\\core\\pylabtools.py:151: UserWarning: Glyph 52380 (\\N{HANGUL SYLLABLE CEON}) missing from current font.\n",
      "  fig.canvas.print_figure(bytes_io, **kw)\n",
      "C:\\Users\\jcc96\\anaconda3\\envs\\ds_study\\lib\\site-packages\\IPython\\core\\pylabtools.py:151: UserWarning: Glyph 45432 (\\N{HANGUL SYLLABLE NO}) missing from current font.\n",
      "  fig.canvas.print_figure(bytes_io, **kw)\n",
      "C:\\Users\\jcc96\\anaconda3\\envs\\ds_study\\lib\\site-packages\\IPython\\core\\pylabtools.py:151: UserWarning: Glyph 50896 (\\N{HANGUL SYLLABLE WEON}) missing from current font.\n",
      "  fig.canvas.print_figure(bytes_io, **kw)\n",
      "C:\\Users\\jcc96\\anaconda3\\envs\\ds_study\\lib\\site-packages\\IPython\\core\\pylabtools.py:151: UserWarning: Glyph 46020 (\\N{HANGUL SYLLABLE DO}) missing from current font.\n",
      "  fig.canvas.print_figure(bytes_io, **kw)\n",
      "C:\\Users\\jcc96\\anaconda3\\envs\\ds_study\\lib\\site-packages\\IPython\\core\\pylabtools.py:151: UserWarning: Glyph 48393 (\\N{HANGUL SYLLABLE BONG}) missing from current font.\n",
      "  fig.canvas.print_figure(bytes_io, **kw)\n",
      "C:\\Users\\jcc96\\anaconda3\\envs\\ds_study\\lib\\site-packages\\IPython\\core\\pylabtools.py:151: UserWarning: Glyph 45824 (\\N{HANGUL SYLLABLE DAE}) missing from current font.\n",
      "  fig.canvas.print_figure(bytes_io, **kw)\n",
      "C:\\Users\\jcc96\\anaconda3\\envs\\ds_study\\lib\\site-packages\\IPython\\core\\pylabtools.py:151: UserWarning: Glyph 47928 (\\N{HANGUL SYLLABLE MUN}) missing from current font.\n",
      "  fig.canvas.print_figure(bytes_io, **kw)\n",
      "C:\\Users\\jcc96\\anaconda3\\envs\\ds_study\\lib\\site-packages\\IPython\\core\\pylabtools.py:151: UserWarning: Glyph 51089 (\\N{HANGUL SYLLABLE JAG}) missing from current font.\n",
      "  fig.canvas.print_figure(bytes_io, **kw)\n",
      "C:\\Users\\jcc96\\anaconda3\\envs\\ds_study\\lib\\site-packages\\IPython\\core\\pylabtools.py:151: UserWarning: Glyph 47560 (\\N{HANGUL SYLLABLE MA}) missing from current font.\n",
      "  fig.canvas.print_figure(bytes_io, **kw)\n",
      "C:\\Users\\jcc96\\anaconda3\\envs\\ds_study\\lib\\site-packages\\IPython\\core\\pylabtools.py:151: UserWarning: Glyph 54252 (\\N{HANGUL SYLLABLE PO}) missing from current font.\n",
      "  fig.canvas.print_figure(bytes_io, **kw)\n",
      "C:\\Users\\jcc96\\anaconda3\\envs\\ds_study\\lib\\site-packages\\IPython\\core\\pylabtools.py:151: UserWarning: Glyph 52488 (\\N{HANGUL SYLLABLE CO}) missing from current font.\n",
      "  fig.canvas.print_figure(bytes_io, **kw)\n",
      "C:\\Users\\jcc96\\anaconda3\\envs\\ds_study\\lib\\site-packages\\IPython\\core\\pylabtools.py:151: UserWarning: Glyph 49457 (\\N{HANGUL SYLLABLE SEONG}) missing from current font.\n",
      "  fig.canvas.print_figure(bytes_io, **kw)\n",
      "C:\\Users\\jcc96\\anaconda3\\envs\\ds_study\\lib\\site-packages\\IPython\\core\\pylabtools.py:151: UserWarning: Glyph 49569 (\\N{HANGUL SYLLABLE SONG}) missing from current font.\n",
      "  fig.canvas.print_figure(bytes_io, **kw)\n",
      "C:\\Users\\jcc96\\anaconda3\\envs\\ds_study\\lib\\site-packages\\IPython\\core\\pylabtools.py:151: UserWarning: Glyph 54028 (\\N{HANGUL SYLLABLE PA}) missing from current font.\n",
      "  fig.canvas.print_figure(bytes_io, **kw)\n",
      "C:\\Users\\jcc96\\anaconda3\\envs\\ds_study\\lib\\site-packages\\IPython\\core\\pylabtools.py:151: UserWarning: Glyph 50577 (\\N{HANGUL SYLLABLE YANG}) missing from current font.\n",
      "  fig.canvas.print_figure(bytes_io, **kw)\n",
      "C:\\Users\\jcc96\\anaconda3\\envs\\ds_study\\lib\\site-packages\\IPython\\core\\pylabtools.py:151: UserWarning: Glyph 50689 (\\N{HANGUL SYLLABLE YEONG}) missing from current font.\n",
      "  fig.canvas.print_figure(bytes_io, **kw)\n",
      "C:\\Users\\jcc96\\anaconda3\\envs\\ds_study\\lib\\site-packages\\IPython\\core\\pylabtools.py:151: UserWarning: Glyph 46321 (\\N{HANGUL SYLLABLE DEUNG}) missing from current font.\n",
      "  fig.canvas.print_figure(bytes_io, **kw)\n",
      "C:\\Users\\jcc96\\anaconda3\\envs\\ds_study\\lib\\site-packages\\IPython\\core\\pylabtools.py:151: UserWarning: Glyph 50857 (\\N{HANGUL SYLLABLE YONG}) missing from current font.\n",
      "  fig.canvas.print_figure(bytes_io, **kw)\n",
      "C:\\Users\\jcc96\\anaconda3\\envs\\ds_study\\lib\\site-packages\\IPython\\core\\pylabtools.py:151: UserWarning: Glyph 49328 (\\N{HANGUL SYLLABLE SAN}) missing from current font.\n",
      "  fig.canvas.print_figure(bytes_io, **kw)\n",
      "C:\\Users\\jcc96\\anaconda3\\envs\\ds_study\\lib\\site-packages\\IPython\\core\\pylabtools.py:151: UserWarning: Glyph 51008 (\\N{HANGUL SYLLABLE EUN}) missing from current font.\n",
      "  fig.canvas.print_figure(bytes_io, **kw)\n",
      "C:\\Users\\jcc96\\anaconda3\\envs\\ds_study\\lib\\site-packages\\IPython\\core\\pylabtools.py:151: UserWarning: Glyph 54217 (\\N{HANGUL SYLLABLE PYEONG}) missing from current font.\n",
      "  fig.canvas.print_figure(bytes_io, **kw)\n",
      "C:\\Users\\jcc96\\anaconda3\\envs\\ds_study\\lib\\site-packages\\IPython\\core\\pylabtools.py:151: UserWarning: Glyph 51473 (\\N{HANGUL SYLLABLE JUNG}) missing from current font.\n",
      "  fig.canvas.print_figure(bytes_io, **kw)\n",
      "C:\\Users\\jcc96\\anaconda3\\envs\\ds_study\\lib\\site-packages\\IPython\\core\\pylabtools.py:151: UserWarning: Glyph 46993 (\\N{HANGUL SYLLABLE RANG}) missing from current font.\n",
      "  fig.canvas.print_figure(bytes_io, **kw)\n",
      "C:\\Users\\jcc96\\anaconda3\\envs\\ds_study\\lib\\site-packages\\IPython\\core\\pylabtools.py:151: UserWarning: Glyph 48324 (\\N{HANGUL SYLLABLE BYEOL}) missing from current font.\n",
      "  fig.canvas.print_figure(bytes_io, **kw)\n"
     ]
    },
    {
     "data": {
      "image/png": "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SEkDABhISQMAGEhJAwAYSEkDABhISQMAGEhJAwAYSEkDABhISQMAGEhJAwAYSEkDABhISQMAGEhJAwAYSEkDABhISQMAGEhJAwAYSEkDABhISQMAGEhJAwAYSEkDABhISQMAGEhJAwAYSEkDABhISQMAGEhJAwAYSEkDABhISQMAGEhJAwAYSEkDABhoV5S0qrqjqr5XVSeq6ujlXg8AwKqNL2lVdVWS/zzJn0tyY5LfqKobL++qAABWa3xJS3JzkhPd/Ufd/feTPJLkrsu8JgCAldoNJe26JC9tun1yGQMA2LOquy/3GrZVVR9Pcnt3/+vL7b+Y5Obu/kubjrknyT3LzV9O8r0L+BXvSfJ3L9Fy15m96nzZ68+Xvf582evPl73+fNnrz7+Q7H+8u/dvdce+S7eelTmZ5PpNtw8keXnzAd39pSRfupjwqjre3YcufnmXJ3vV+bLXny97/fmy158ve/35steff6myd8PLnc8luaGqPlBVv5DkcJLHL/OaAABWavyZtO5+var+7SRPJbkqyYPd/fxlXhYAwEqNL2lJ0t2/m+R3VxR/US+TDshedb7s9efLXn++7PXny15/vuz151+S7PEbBwAArkS74T1pAABXHCUNAGAgJQ0AYKBdsXHgUqqqv3qeQ17t7v9iYr7s9efLXn++7PXny15/vuz15+/K7O6+on6ysUv06iTveouf/2Fqvuy9tfbdmr2b175bs3fz2ndr9m5e+27N3s1rX1X2FXcmLckb3f333urOqurB+bLXny97/fmy158ve/35stefv+uyr8T3pJ3viXq7f2CrzJe9/nzZ68+Xvf582evPl73+/F2XfSWeSfv5qrr6Le6rbHyrwdR82evPl73+fNnrz5e9/nzZ68/fddlXYkn7m0n+8jb3Pzk4X/b682WvP1/2+vNlrz9f9vrzt8uuFWbnYrOvxJKWbPyHsVvzZa8/X/b682WvP1/2+vNlrzf/I0kOb5P/UJKL3pm6Te7Fezu7MHbjT+xM2VPZu3ntuzV7N699t2bv5rXv1uzdvPbdmr2Gtf+P57n/d6at+0o8k2Znyt7KXnW+7PXny15/vuz158tef/755o57Xq7EkrbK/5BWnS97/fmy158ve/35stefL3v9+avcOLCSdV+JJc3OlL2Vvep82evPl73+fNnrz5e9/vwzb+5/q/eO/d7byLa78xJZ5e6OVefLXn++7PXn78XdXat+zvM283fr87JX/86v1H9DK83v7r92sXN3YCXrvhJL2qp3d6wyX/b682VfnvzduLtr1c9Jtsl+u3br87Kb/879G7o8+auyknVfiSVtN7/pUfb682WvP3+V/yW9m59zz8t6s1ed79/Q5clfFRsHLpHd/KZH2evPl73+/N26u2vVz7nnZb3Zq873b+jy5K+KjQOXyG5+06Ps9efLXn/+bt3dtern3POy3uxV5/s3dHnyV8XGgUtklbs7Vp0ve/35stefv1t3d636Ofe8rDd71fn+DV2e/FVZybpr+aRcgBGq6r689f/TrySvdPfENw6vlOeFnfK3sndciWfSgNl26+6uVfO8sFP+VvYIJQ2YZrfu7lo1zws75W9lj/i5y70AgHPs1t1dq+Z5Yaf8rewRzqQB0+zW3V2r5nlhp/yt7BFKGjDNbt3dtWqeF3bK38oeYXcnAMBA3pMGADCQkgYAMJCSBgAwkJIGADCQ3Z0A56iq30pyS5LXl6F92dgx9zNj3f1b614fcGVQ0gC2dri7/yRJquoXs/GRBluNAayElzsBAAZS0gAABlLSAAAGUtIAAAZS0gAABlLSAAAG8hEcAD/r1SQPV9U/WG7/XJLfe4sxgJWo7r7cawAA4Bxe7gQAGEhJAwAYSEkDABhISQMAGEhJAwAY6P8HV15uKCmqAsAAAAAASUVORK5CYII=",
      "text/plain": [
       "<Figure size 720x720 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "data_result['인구수'].plot(kind='bar', figsize=(10, 10))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 220,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:ylabel='구별'>"
      ]
     },
     "execution_count": 220,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAoYAAAI+CAYAAAAhE8thAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjUuMCwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy8/fFQqAAAACXBIWXMAAAsTAAALEwEAmpwYAAA5IElEQVR4nO3df5ydZ13n/9c70yaFhoQikc0PaBCygliLEhV8VCxrI8WCBBB0sWrdxYGyKBGohsYF3IUluwjyXXEpIUJZFPtLCcrQlGkxXUALTgGNaLqKhpYoX4qBSJpCk/Szf5x74M7pJJmZnMk5c+b1fDzm0XNf93Vf53NuC7y9rvtHqgpJkiRpUb8LkCRJ0mAwGEqSJAkwGEqSJKlhMJQkSRJgMJQkSVLDYChJkiQAzuh3AYPm4Q9/eK1du7bfZUiSJJ3U7bff/uWqWtGr8QyGXdauXcvExES/y5AkSTqpJJ/v5XguJUuSJAkwGEqSJKlhMJQkSRJgMJQkSVJj3t98kuTZVfWBXo23e98B1m4e69VwkjQU9m69pN8lSDoNBiIYJrkEuKLZPBcIsLfZfktV/XGS/wF8X9N2DvD+qno98EvAMcEwyQ5gadfXnA+sqqrDPf8BkiRJQ2AggmFVjSW5BXg+8FQ6S9wfBa6tqnubbr8NnN18/gHgUScYb2N3W5Ix4EgPy5YkSRoqAxEMk7wQeDRwY1W9t2l7GvCbSe6sqv8OvBu4rXXYePPPkSS7aGYWT/Q9VVU9L16SJGlI9D0YJtkAjDabG5J0d3lCkr9sPr+VzjLzCHBOkocAR6vqoml81dEelCtJkjS0+h4Mq2qcb83+keRS4IyqurrdL8m/ATYB9wOHgf10ri082OqzAdjSOmwNcKjpSzOzuLWqdvb+l0iSJM1vfQ+Gk5KcC7wKeFpnM+uBN1XV5wGq6uokK4CXAU+iU/tjgFdOjjFFyNwE7DlZEEwySjNrObKsZ68blCRJmlcG6TmG1wA30Lnz+HuB64Fru/q8j851hj8NPKfZf02SM0/li6tqW1Wtr6r1Iw9efipDSZIkzVsDM2NI57rBT1fVfQBJPsUDg+sy4Laq+nrT5zPAfcBZdJaXJUmSNEuDFAyvAK5v3XwS4Ne6+ryCzgzh5PYZwJur6munpUJJkqQhNjDBsKpuBW49SZ+PA0+fwbDbcSZRkiRpWgYmGM6Fqjp48l7HOm/1ciZ89ZMkSVqABunmE0mSJPWRwVCSJEmAwVCSJEkNg6EkSZIAg6EkSZIaBkNJkiQBBkNJkiQ1DIaSJEkCDIaSJElqGAwlSZIEGAwlSZLUGOp3Jc/G7n0HWLt5rN9laBr2+k5rSZJ6al4FwySXAFc0m+cCAfY222+pqj9u+u0AlnYdfj6wqqoOz32lkiRJ88+8CoZVNZbkFuD5wFPpLIV/FLi2qu5t9dvYfWySMeDIaSpVkiRp3plXwTDJC4FHAzdW1XubtqcBv5nkzqr67yc6vqrqNJQpSZI0L82bYJhkAzDabG5I0t3lCUn+sqp2HmeIo3NWnCRJ0hCYN8GwqsaB8cntJJcCZ1TV1a22DUl2tQ5bAxwC9jf7dwFbu8NjklGa0DmybMXc/ABJkqQBN2+C4aQk5wKvAp7W2cx64E1V9fkpwuMmYM8JZhEBqKptwDaAJSvXudwsSZIWpPn4HMNrgBuA7wO+F7geuLavFUmSJA2BeTdjCIwAn66q+wCSfIr5GXAlSZIGynwMhlcA17duPgnwa/0rR5IkaTjMu2BYVbcCt06z+3bAB1pLkiRNw7wLhjNRVQdnesx5q5cz4avWJEnSAuS1eZIkSQIMhpIkSWoYDCVJkgQYDCVJktQwGEqSJAkwGEqSJKlhMJQkSRJgMJQkSVLDYChJkiTAYChJkqTGUL8SbzZ27zvA2s1j/S5DkjQA9vqKVC0w837GMMm5SS7odx2SJEnz3cDMGCZ5CvBf6ITVAPcDr6uqjzX73wyc33XY65t/XgB8rDXWDmBpV9/zgVVVdbjnxUuSJA2BgQmGwFuAZ1fVlwCSfDvwIWA9QFW9MsmNVfWMJJcBXwNeCjwGeH97oKra2D14kjHgyFz+AEmSpPlskJaSPw48K8mjk3wH8Mymre1o888lwL1V9QLgldP9gqqqnlQqSZI0hAZmxrCqXpVkPfCjQAF/VVXv6up2f/PPs4CvJ7mOKWYMj+PoybtIkiQtXH0Phkk2AFuOs2/y41bg+4CvJfl1YDWwCvgj4It0rjGcaqw1wCFgf7N/F7C1qnZ2fc8oMAowsmxFD36VJEnS/NP3YFhV48D4NLruBEiyEfhO4DuAc4EPA7851VhJNgF7uoPgFDVsA7YBLFm5zuVmSZK0IA3MNYbNXccn6/Nc4PnAf6ZzDeKvAI8HLp/b6iRJkobfwARD4EnT6LMKmKiqvVV1uKr+GfgonaVlSZIknYK+LyW3PKq5BrDbz1TVvubzNmBrklvo3EyyCNgLvOK0VChJkjTEMsxPcEmyFDhcVd+Y7jHr16+viYmJOaxKkiSpN5LcXlXrezXeIM0Y9lxVHex3DZIkSfPFIF1jKEmSpD4yGEqSJAkwGEqSJKlhMJQkSRJgMJQkSVLDYChJkiTAYChJkqSGwVCSJEmAwVCSJEkNg6EkSZKAIX8l3mzs3neAtZvH+l2G1Fd7t17S7xIkSX0wMMEwySOA/wSc1zT9NfA7VfXFkxz3nqr6+bmuT5IkadgNTDAE3ge8sfkD+CHgD4CntTsl+WBVPbPVtLp7oCQ7gKVdzecDq6rqcK8KliRJGiaDFAyXAJ+sqnsBkvxF0/ZNSZbywMD3AFW1sbstyRhwpCeVSpIkDaFBCoZXAHck+TSdm2KeCDy3q8/TgCck+faq+lLTliQ/DfxFVX3uRF9QVdXjmiVJkoZG3+9KTscZwF8BnwJ+AngmcDvwl0nOaPosA14GPAf47SRntoY5Apws9B09QQ2jSSaSTBw9dOBUfo4kSdK8NQgzhk8GXtx8vhvY3vr8O83n7cB/BjZX1aebIPl7zUxhVdUNAEk2AFtaY68BDgH7m/27gK1VtbNdQFVtA7YBLFm5zllFSZK0IPU9GFbVnwN/nmQl8Et8667kzwK/XVX7mtnB/wB8qTlmV5Jbq6qStMcaB8Ynt5NsAvZ0B0FJkiQ9UN+XkluuBXYBP9X8faRpo6oOV9U+4MbJzpPXC1bVRae9UkmSpCHU9xnDlgcBH6+qQwBJPg4sSRJvGpEkSZp7gxQMrwTen2QyBC4CruwOhc11gt1e3SxJS5IkaZYyzJNxzXMPD1fVN6Z7zPr162tiYmIOq5IkSeqNJLdX1fpejTdIM4Y9V1UH+12DJEnSfDFIN59IkiSpjwyGkiRJAgyGkiRJahgMJUmSBBgMJUmS1DAYSpIkCTAYSpIkqWEwlCRJEmAwlCRJUmOo33wyG7v3HWDt5rF+lyFJp9XerZf0uwRJA6AvM4ZJliVZ3Y/vliRJ0tTmdMYwyUOAq4BHAI8CvgZ8BTgHeD/w+qbfHcBdXYcfqKrntcZ6LvDS43zVO6rq+lbfHcDSrj7nA6uq6vBsf48kSdIwm+ul5F8HrqmqP0myBLgVeDmwArig1e+uqrroRANV1R8l+Qjw9Kq6FiDJ84Fbqmp/V9+N3ccnGQOOnMqPkSRJGmZzvZS8FvhTgKr6BvBxpg5nK5LsmuJvpKvfmcCzWtvPBBZPt5iqqhlVL0mStIDM9Yzhe4DfSPIm4DHAD9FZ0j0HeH+Ss4CHAk8/zvErkhyoqnub7Xs4dol4adM2HUdnWLskSdKCMqfBsKo+lOQLwM8AdwP/rqruTfLDwFOAxwE/fZJhrgduT3I58FPAsiSfBgLcD/xJkhuq6m1JNgBbWseuAQ4B+wGS7AK2VtXO9hckGQVGAUaWrTiVnyxJkjRv5XSsriZ5GfBsoOgsX38GeE1VHWr2r6ZzY8l3NYf8DfC/qmrfcca7FDijqq4+yfduAvZ0B8ETWbJyXa38+bdOt7skDQUfVyPNT0lur6r1vRpvzh9Xk+QFwGOBZ1TVjzU3mXwGeGOr2/XALcAL6cwujgM3zHVtkiRJ+pbT8YDrBwH/WlXtm072N+00N5gsBj45eS1hkgngzCRnVtXhKZaIafpd1tp8wBKxJEmSpu90BMP3Aq9pru+7Dxih88zCXwGoqqNJXk3nZpT2DOaWyWcOVtU4nVlESZIkzZE5D4ZVdT/wupP0mavgtx3wgdaSJEnTMNTvSq6qgzM95rzVy5nwImxJkrQA9eVdyZIkSRo8BkNJkiQBBkNJkiQ1DIaSJEkCDIaSJElqGAwlSZIEGAwlSZLUMBhKkiQJMBhKkiSpYTCUJEkSMMCvxEvypKq6fYr291TVz7e2fwJYUlXX9+J7d+87wNrNY70YSpI0QPb6ulPppPoeDJM8BfhvwBHgHmC0qr4EvAG4uNXvncA5wAVJbmiaLwceDJzVNeYOYGnXV50PrKqqw3PwMyRJkua9vgdD4DeBn6iqf0nyw8B/AV4CkORm4Ler6gPAy+ksfY8BlzXH3jPVgFW1sbstyRid8ClJkqQpDMI1hvdU1b80nz8DPHxyR1Vd1IRCquoQ8HXg8cAa4OnAjcDm6X5RVVWPapYkSRo6gxAMP5TkN5L8OPDbwFsmdyS5OcmzW31fCbwdeDMwVlUXA1un+T1He1WwJEnSMOr7UnJVvTXJWuDRwCuqan+z6/+fvMkkyZnAK4DHVNVokqfTCZS/0B4ryQZgS6tpDXAI2N/s3wVsraqdc/iTJEmS5qW+B8PGEjrB78FJAgT4H639BewD3pHk7Kq6KcmngS8DT/lmp6pxYHxyO8kmYM/JgmCSUWAUYGTZip78IEmSpPlmUILh24GXVNX/BUiyFPhIklur6lBVHQF+L8lL6ITBG5o7lwGuOdUvr6ptwDaAJSvXeR2iJElakAbhGkPozAje3+8iJEmSFrJBmTF8KfBbSc5utgO8trkTudtrmpnDtpuq6k1zWqEkSdKQG4hgWFV3AM+aRr+rgKtmMPR2wAdaS5IkTcNABMO5UlUHZ3rMeauXM+FrkyRJ0gI0KNcYSpIkqc8MhpIkSQIMhpIkSWoYDCVJkgQYDCVJktQwGEqSJAkwGEqSJKlhMJQkSRJgMJQkSVLDYChJkiTAYChJkqTGvH9XcpJnA39cVdWL8XbvO8DazWO9GEqSJC1Qe7de0u8SZmXggmGSXwUWVdXWVtsjgXdP0f2VwC8BY8CRVv8dwNKuvucDq6rqcK9rliRJGgYDEwyTPAQYBVYAh5NsAt5ZVfdU1V1JNgLnV9XHk3wvsK+qvpTkAWNV1cYpxj8mPEqSJOlYAxEMk7wM+A7gfXTC20jztzXJvmb28KHALwAfB54DfBD40ky+p1fLzZIkScOo78EwyTnAx5o/gB+nU9cfA7/b9HkYcBhY3PQ5E7ivNczvJ/lwVf3uCb7qaC/rliRJGjZ9D4bAKuDi1vb9dEJfu20M2Me3guFiOkFx0gur6miSDcCWVvsa4BCwHyDJLmBrVe1sF5BklM4yNiPLVpziz5EkSZqf+h4Mq+qzwGeTrAZeAXxXs+tvgd9qri9cAzwReESSJwOPBM5LsmRymGascWB8cuzmOsU93UFwihq2AdsAlqxc53KzJElakPoeDFveB/wq8Mlm+weAPwAuoDPz9z3AB4AnA38GnMO37jw2zEmSJJ2iQQqGDwL+dvIGkSR/AywBqKrbgNumOiiJN5VIkiT1wCAFwyuA61uPnwnwa/0rR5IkaWEZmGBYVbcCt87iuItOsHs7x96kIkmSpOMYmGA4F6rq4EyPOW/1cibm6WtsJEmSTsWifhcgSZKkwWAwlCRJEmAwlCRJUsNgKEmSJMBgKEmSpIbBUJIkSYDBUJIkSQ2DoSRJkgCDoSRJkhoGQ0mSJAFD/kq82di97wBrN4/1uwxJ0hT2+spSaU4N9Ixhkocn+bf9rkOSJGkhGKhgmOSDXU3fDbygtf/mKY7ZOUXbjiQ3d/3dneTM3lctSZI0HAZmKTnJCLC+CW/PBS4HHgrc0Oq2dopweG73WFW1cYrxx4AjvapXkiRp2AxMMKQTBN8LvLaqfh24NsmFwAWtPgeAa7qOG53uF1RVnWKNkiRJQ6vvwTDJIjqhcHVVXZHkF5L8LvCyKbq/EOheDv7oNL/q6CmUKUmSNPT6HgyBxcCXqup3AKrq3UnGq+reJIeALyfZAGxpHfMIIMAXAZIAbKUT/tr91gCHgP1Nv13A1qo65rrEJKM0M48jy1b0+vdJkiTNC30PhlX1deD6ZubwSuDHgKPNNYefBjZX1b3A+OQxSS4Fzqiqq6cYst1vE7CnOwhOUcM2YBvAkpXrXG6WJEkLUt+DYcvPAcuBC6vqfvjmTN5rgFcnWQFc3z4gyWXAuqpafZprlSRJGjqDFAwBDk2GwsbXJj9U1d3Ahd0HTPW4GkmSJM3cIAXD9wCvSfIROo+VGQHuAF7V16okSZIWiIEJhs2jZH5jFof+0gn2bQcOz64iSZKkhWVgguFsVdXfnWDfwZmOd97q5Uz4Lk5JkrQADdQr8SRJktQ/BkNJkiQBBkNJkiQ1DIaSJEkCDIaSJElqGAwlSZIEGAwlSZLUMBhKkiQJMBhKkiSpYTCUJEkSMASvxOu13fsOsHbzWL/LkDQH9vq6S0k6oYGeMUzy8CT/tt91SJIkLQQDNWOY5INV9cxW03cDFwCvb/b/A3Bn12H3VtUzusbZASzt6nc+sKqqDve0aEmSpCExMMEwyQiwPsmZwHOBy4GHAje0ut1ZVReebKyq2jjF+GPAkV7UKkmSNIwGJhjSCYLvBV5bVb8OXJvkQjozhpMWJbmZzmxggK817c+uqntO9gVVVT2tWJIkaYj0PRgmWUQnFK6uqiuS/EKS3wVe1t23qp7aHHMpcEZVXT2Drzrai3olSZKGVd+DIbAY+FJV/Q5AVb07yXhV3ZvkEPDlJE8GXtQ6ZhGQJO3ZxHcBZwNbWm1rgEPAfjoH7AK2VtXOdgFJRoFRgJFlK3r52yRJkuaNvgfDqvo6cH0zc3gl8GPA0eaaw08Dm6vqXuC2JKvpzCQ+oTn8s8Dbqmpfa8jxyQ9JNgF7uoPgFDVsA7YBLFm5zuVmSZK0IA3S42p+DlgOXFhVT2uWjT8LvKbV5zpgJ/CTzd+NwPWnu1BJkqRhNEjBEOBQVd3f2p68uWTyruUlwO1VdV9V3Qd8Cljc3MksSZKkU9D3peSW9wCvSfIROo+VGQHuAF4FUFVHk2wBPpCkfdwWn00oSZJ06jLMT3BJshQ4XFXfmO4x69evr4mJiTmsSpIkqTeS3F5V63s13iDNGPZcVR3sdw2SJEnzxaBdYyhJkqQ+MRhKkiQJMBhKkiSpYTCUJEkSYDCUJElSw2AoSZIkwGAoSZKkhsFQkiRJgMFQkiRJDYOhJEmSgAF/JV6S1cDKqjptLy/eve8AazePna6vkyS17N16Sb9LkBa0gQqGSXZW1cWtpnXABcBEV79LgbOqavtxxtkBLO1qPh9YVVWHe1exJEnS8BioYAgsPt6OJM8AXtlsPhKoJD/dbL+1qj442beqNk5x/BhwpHelSpIkDZeBCYZJAqxPshj4AeAiYC3w9wBVdSNwY9NvB3A/8Nyqqul+x0z6SpIkLTSDdPPJBuALwHOAPcANwK3tDklWAVcD7wWuAX4vyaOmOf7RnlUqSZI0hAZixjDJGcAvA08H3g3srKq/TvJwYHXT53XN5/8K7G8OvR34z0m+WlVXJNkAbGkNvQY4NNk/yS5ga1Xt7Pr+UWAUYGTZirn4iZIkSQOv78GwCYVvB7ZX1V1JXg1c39xg8k1V9brWMZc1bVcDv9jqMw6Mt/ptAvZ0B8FuVbUN2AawZOU6l5slSdKCNAhLyauAW6pqB0BV/QVwJWBAkyRJOo36PmNYVXcCd3a1TQB07jOBKZaIJ9sva20+YIlYkiRJ09f3YDgd3UvEkiRJ6r2BDoZVtQvYdQpDbAd8oLUkSdI0DHQwPFVVdXCmx5y3ejkTvpJJkiQtQINw84kkSZIGgMFQkiRJgMFQkiRJDYOhJEmSAIOhJEmSGgZDSZIkAQZDSZIkNQyGkiRJAgyGkiRJahgMJUmSBAz5K/FmY/e+A6zdPNbvMiT10V5fiylpgerLjGGS1UnWn6TP2Ul+9HTVJEmStNCdlhnDJDur6uJW0zrgAmAiyc5WHfur6gVN24uAnwVuaY1zB/DPXcOvqarHdn3fDmBpV7/zgVVVdfhUf48kSdIwOl1LyYtPtLOqLprmOP/YFTBpQmT3eBu725KMAUem+T2SJEkLzpwHwyQB1idZDPwAcBGwFvj7WQy3NsnNXW3nTvfgqqpZfKckSdKCcDpmDDcAXwCeQ2dZ+KvA9wOrT3DM9wLbgS+2G6vqcadQx9FTOFaSJGnozWkwTHIG8MvA04F3Azur6q+TPJwTB8PPAC8GfqMZZwOwpbV/hM6NM+3rBbfSCX/tfmuAQ8D+ZpxdwNaqOmb5OckoMAowsmzFTH6iJEnS0JizYNiEwrcD26vqriSvBq5PcukUfR9LJ+ydDfwDULRm+KpqHBhv9X8msLaq3jbFV7f7bQL2dAfBblW1DdgGsGTlOpebJUnSgjSXj6tZBdxSVTsAquovgCvphL629wOXAz9PZ2Zx2fEGTHJd8/Fe4GCP65UkSVrQ5mzGsKruBO7sapsA6NyP8s22d3Qf297f5WHNMbccr4MkSZJmZ769+eT8Ke5KBvi5qvqn016NJEnSEOlLMKyqXcCuE+yffFbhZV3tM70zZDvH3qAiSZKk45hvM4YzUlUzvg7xvNXLmfA9qZIkaQHqy7uSJUmSNHgMhpIkSQIMhpIkSWoYDCVJkgQYDCVJktQwGEqSJAkwGEqSJKlhMJQkSRJgMJQkSVLDYChJkiRgyF+JNxu79x1g7eaxfpchSbO219d6SpqlgZ4xTPLsftcgSZK0UAzEjGGSjwD3t5qOVNXFwC8BH2j6PBd46XGGeEdVXd8abwewtKvP+cCqqjrcq7olSZKGyUAEQ+D+qrpociPJzu4OVfVHTYB8elVd2/R7PnBLVe3v6rux+/gkY8CRXhcuSZI0LAZ6KXkKZwLPam0/E1g83YOrqnpekSRJ0pAY9GC4KMkNSV7SbN/DsUvES5u26Tja08okSZKGzKAsJR/P/VX1kwBJLgd+CliW5NNA6FyX+CdJbqiqtyXZAGxpHb8GOATsb8bYBWytqmOWqpOMAqMAI8tWzO0vkiRJGlCDEgwXJfnNE3WoqrcDbwdIcilwRlVd3dVnHBif3E6yCdjTHQSnGHsbsA1gycp1LjdLkqQFaVCC4QuBs1rb9/arEEmSpIVqIIJhVX3xRPunWCKebL+stfmAJWJJkiRN33GDYZItQPey6k7gYoCq+m9J3lRVV8xhfTTfdcwSsSRJknovx3uCS5IfAR4NPBZ4JPAu4PHAQ4CfrKofTPKnVfW001XsTCVZChyuqm9M95j169fXxMTEHFYlSZLUG0lur6r1vRrvuDOGVXVrkruBw3TuDr41yeOAvwEO9KqAuVRVB/tdgyRJ0nxxsmsM3wI8Btib5C3AnrkvSZIkSf1wwgdcN+8r3lFVG5j6AdE+2kWSJGlITOfNJ1OFvyS5Eji3x/VIkiSpT064lJzkp4DvTPKCpu8fA/cBdwHnAB+f8wolSZJ0WpzsGsOzgD8CHgRc23re4P45rUqSJEmn3QmDYVW9p72d5Meq6sNzW5IkSZL64YTXGCYZ6WraPIe1SJIkqY9OtpT8T0k+2Xy+f66LkSRJUv+cLBj+VVU9a3IjyUfmuB5JkiT1ycmCYfejar4tyY91tf1pVR3uYU2SJEnqg5MFw24PBh4HpNku4GN0XpvXF0meVVV/0qvxdu87wNrNY70aTpLmrb1bL+l3CZJOs5kGwy9U1f+ci0KS/ANwZ1fzvVX1jGb/rqbtPGA3sK+qfgb4T8AxwTDJDmBp11jnA6uc3ZQkSZrayYLhPV3bc/kKvDur6sLj7ayqC5M8CPjsifo1fTd2tyUZA46cYo2SJElD62TvSn5OV1Om7NijWpLcnOS2JJ9oPt+c5OxWn1cCO5K89Jiikl1Jumt9gKry3c6SJEnHMdOl5DfMSRVAVT0VIMmlwBlVdfXkviRL6DxD8V+q6vVJXpHkrXSCIiebQWwc7XXNkiRJw2RGwbCqbu51AUmeDLyo1bSo05wLWm3vBsar6s+aOt6SZGVVHU3y162xNgBbWsetAQ7RvMKvuU5xa1Xt7KphFBgFGFm2olc/TZIkaV6Z6Yxhz1XVbcBtSVYDLwOe0Oz6LPC2qto32bd1A8rkdvdY48B4a/8mYE93EJyihm3ANoAlK9e53CxJkhakvgfDluuAK4HXNttPBq4Hfmiyw1RLxklOGPokSZI0PSe8+eR0ad7JvAS4varuq6r7gE8Bi5Oc2d/qJEmSFoaBmDFsrhXcAnyga3l4yzSeO/i3c1eZJEnSwjEQwRCgqm4CbprFcb9ygt3b6eNbWSRJkuaTgQmGc6GqDs70mPNWL2fC10BJkqQFaCCuMZQkSVL/GQwlSZIEGAwlSZLUMBhKkiQJMBhKkiSpYTCUJEkSYDCUJElSw2AoSZIkwGAoSZKkhsFQkiRJwJC/Em82du87wNrNY/0uQ9ICttfXckrqk4GdMUxydpIf7XcdkiRJC8Wczxgm+Qfgzq7me6vqGc3+na069lfVC5q2FwE/C9zSGusO4J+7xlpTVY/t+s4dwNKufucDq6rq8Cn8HEmSpKF1OpaS76yqC0/UoaoumuZY/1hVF7cbmhDZPd7G7rYkY8CRaX6PJEnSgnM6guGiJDfTmcEL8LWm/dlVdc8Mx1rbjNV27nQPrqqa4fdJkiQtGHMeDKvqqQBJLgXOqKqrp3HY9wLbgS92jfW4Uyjl6CkcK0mSNPTmLBgmeTKd6wQnLeo054JW27uOc/hngBcDv9GMtQHY0to/0ozXvl5wK53w1+63BjgE7G/G2QVsrapjlp+TjAKjACPLVpz0t0mSJA2jOQuGVXUbcFuS1cDLgCc0uz4LvK2q9gEkIclj6YS9s4F/AIrWDF9VjQPjk9tJngmsraq3TfHV7X6bgD3dQXCKWrcB2wCWrFzncrMkSVqQTsfjaq4DdgI/2fzdCFzf2v9+4HLg54GnA8uON1CS65qP9wIH56JYSZKkhWpOrzFMMgIsAW6vqvuatk8Bi5OcWVWHq+odUxx3vCEfBlBVtxyvgyRJkmZnToNhVR1NsgX4QFfY2zLL5wmeP8VdyQA/V1X/NKsiJUmSBJyeu5JvAm6a4TGTzyq8rKt9pneGbOfYG1QkSZJ0HEP9ruSqmvF1iOetXs6E7ymVJEkL0MC+K1mSJEmnl8FQkiRJgMFQkiRJDYOhJEmSAIOhJEmSGgZDSZIkAQZDSZIkNQyGkiRJAgyGkiRJahgMJUmSBAz5K/FmY/e+A6zdPNbvMiTNY3t9raakeWpggmGS/wv8U1fz3VX1/FafceBnu/r8XlVd1DXWDmBpV7/zgVVVdbg3FUuSJA2XgQmGwJ3dAW8KDwF+sqttWXenqtrY3ZZkDDgy6+okSZKG3CAFw+l4CLCxq+0BwfB4qqp6Wo0kSdIQmRfBMMkiYDHwpKbp39Op/b3N/rOAw1V19ATDnGifJEnSgjdIwfArSXYBjwACfLFpfwZwHvAfpjjmSa3P70myFNjSalsDHAL2AzTjb62qnT2tXJIkaQgMTDCcvMkkyaXAGVV1dWv3J4FPJlkFvAx4PJ3w+DfA26qqfdPK+OSHJJuAPScLgklGgVGAkWUrTvm3SJIkzUfz7TmG19AJfi+ks5z8YeDaUx20qrZV1fqqWj/y4OWnOpwkSdK81PcZwyQbOHb5d7L9stbm5PLvg4BPVtW9TZ9PAmcliTeWSJIknZq+B8OqGqe1/HsSVwLvTzIZAgNcaSiUJEk6dX0PhjMxwxAJsB3wgdaSJEnTMK+C4UxV1cGZHnPe6uVM+DorSZK0AM23m08kSZI0RwyGkiRJAgyGkiRJahgMJUmSBBgMJUmS1DAYSpIkCTAYSpIkqWEwlCRJEmAwlCRJUsNgKEmSJMBgKEmSpMa8f1dyktXAuVX1Z70Yb/e+A6zdPNaLoSRJGjh7t17S7xI0wAYmGCbZWVUXn6TPa4F/BxwBvgj8IvBo4CLgz1r9dgBLuw4/H1hVVYd7WLYkSdLQGJhgeDJJHg+sq6ofabZfCvwM8Lfdfatq4xTHj9EJlJIkSZrCfLrG8PPAsiSXJHkqnZnDP5/JAFVVc1KZJEnSEBikGcMnJdk1RfuLqurvq+pQkucDPwqsBq4E7gUeNs3xj/amTEmSpOE0MMGwqlYAJLkUOKOqrp7cl2QJcBWdcPcw4N8AfwocBD7d6rcB2NIadg1wCNjf7N8FbK2qne3vTjIKjAKMLFvR2x8mSZI0TwxMMDyRqvoG8AsASZ4MXAy8D3gF8IPAZ5p+48D45HFJNgF7uoPgFONvA7YBLFm5zuVmSZK0IM2nawxJ8jbgfuCTwBeAtwLX9bMmSZKkYdH3GcMpln8n2y9rbU4u/z4UuLOqPtm072n+JEmSdIr6Hgy7l3+n4bok93W1faqqfrWHZUmSJC04fQ+GM1FVl87wkO2AD7SWJEmahnkVDGeqqg7O9JjzVi9nwtcFSZKkBWhe3XwiSZKkuWMwlCRJEmAwlCRJUsNgKEmSJMBgKEmSpIbBUJIkSYDBUJIkSQ2DoSRJkgCDoSRJkhoGQ0mSJAHz8JV4Sd5TVT/f2v4JYElVXd+L8XfvO8DazWO9GEoaSnt9ZaQkDa2BCYZJrgMe1tW8rqrObfa/EzgHuCDJDc3+y4EHA2d1jbUDWNo11vnAqqo63OPSJUmShsLABMOqekF3WysAArycztL3GHBZ03bPccbaOMVYY8CRU61TkiRpWA36NYbfrK+qDgFfBx4PrAGeDtwIbJ7uYFVVvS5QkiRpWPR9xjDJBmDLcXavTLIL2FpVO4FXAm8H3gw8r6r+MMlP07WUfBxHe1GvJEnSsOp7MKyqcWD8RH2SnJnk14DHVNVokqcDH0ryC139ukPmGuAQsL/Zv4tvhUxJkiS19D0YTkryGeDLXc1rqupxQAH7gHckObuqbkry6ab/UyY7d4fMJJuAPScLgklGgVGAkWUrTv3HSJIkzUMDEwyBL1fVRe2GJDsBquoI8HtJXkInDN5QVV9qul1zql9cVduAbQBLVq7zOkRJkrQgDfrNJ5IkSTpNBmnG8FHNNYBt3zFFv9c0M4dtN1XVm+amLEmSpIVhYIJhVf3bafS5CrhqBsNuB3ygtSRJ0jQMTDCcC1V1sN81SJIkzRdDHQxn47zVy5nwXbCSJGkB8uYTSZIkAQZDSZIkNQyGkiRJAgyGkiRJahgMJUmSBBgMJUmS1DAYSpIkCTAYSpIkqWEwlCRJEmAwlCRJUsNX4nXZve8AazeP9bsMSVow9voaUmlgDEwwTLIDWNrVfD6wqqoOJzkTuHGKQ58I/JuqOjLdsXpVsyRJ0jAZmGBYVRu725KMAUea/YeBi6bos3OmY0mSJOmBBiYYHk9VFUCSBwFjwP1dXb4HqJmMJUmSpAca9GB4tPV5BDhUVc/swViSJEnq0vdgmGQDsKXVtAY4BOxv9u8CtgIfA34wyc1TDLO5qiamO1ZVPWD5WZIkaaHrezCsqnFgfHI7ySZgz3HC24qmz6XAGVV19SmMRavfKDAKMLJsxWx+hiRJ0rzncwyBqtpWVeurav3Ig5f3uxxJkqS+6PuM4XRMsUQ82X5Za9MlYkmSpFMwL4Jh9xKxJEmSem8Qg+F2oFcPoe7lWJIkSUNt4IJhVR3s51jnrV7OhK9nkiRJC5A3n0iSJAkwGEqSJKlhMJQkSRJgMJQkSVLDYChJkiTAYChJkqSGwVCSJEmAwVCSJEkNg6EkSZIAg6EkSZIaBkNJkiQBA/iu5LYkPwrcVlX3nKDPDwOLq+qWXnzn7n0HWLt5rBdDSVLP7PUd7pJOg4EIhkleAfx4q+l7qurbgZ8F7gDuSfJW4InAdwJ7gW8ALwVWA2d1jbcDWNr1NecDq6rqcM9/gCRJ0hAYiGBYVW9J8v8BZ1fVvya5eYo+mwCS/CHwG1X1V83290zRd2N3W5Ix4EiPS5ckSRoag3SN4SOBtzSf27N6f5DkPwIkORt4PPD82XxBVdUpVShJkjTE+h4MkzwiyffTWSZ+RJIfAf5nku9ruvz7qvrd5vMbgZcDj0py4Qy/6mgPypUkSRpag7CU/Ajg++kEt/cDa4B76QpySf4X8HdVNZ7k/wDvTHJvV58NwJZW0xrgELC/2b8L2FpVO7uOGwVGAUaWrejZD5MkSZpP+h4Mm2sF/yrJOuAVwHc0uz4P/C7wz832G4FDSZZX1QHg5wCSPLo11jgwPrmdZBOwpzsITlHDNmAbwJKV61xuliRJC1LfgyFAkjOA9wH/sXVTyXcDVwM/BBytqruSvAT4MnDD5LFVdc3pr1iSJGn49P0aw8bi5p+fa7V9js5NKIsf2F2SJEm9NhAzhlV1KMlrgR1J7m+aFwFvqKqDXd1f08wctt1UVW+a80IlSZKG2EAEQ4Cq+hDwoZP0uQq4agbDbufYR99IkiTpOAYmGM6FKWYbT+q81cuZ8NVTkiRpARqUawwlSZLUZwZDSZIkAQZDSZIkNQyGkiRJAgyGkiRJahgMJUmSBBgMJUmS1DAYSpIkCTAYSpIkqWEwlCRJEjDkr8Sbjd37DrB281i/y5AkLQB7fQWrBsxAzxgm2Z5k7Un6POk0lSNJkjTUBmLGMMlm4OJW0+OAJ3b1eQqwFbgf+FfgF6vqS8Abuo4lyQ5gadfXnA+sqqrDvaxdkiRpWAxEMKyqrXRCHwBJrgO6A9xvAs+uqi8n+RHg9cDoccbb2N2WZAw40quaJUmShs3ALCUneXiS/9Fsnk1nVhBgWZKzgHuq6stN26eBc1rH7krynJN9R1VVL2uWJEkaJgMxY9g4A1jVfH5zVR1OAvAa4FpgR5I3A7cDzwQmQyRVdeE0xj/a02olSZKGTN+DYZIfAi4DHgI8OckfAEuSXNB0eVVV7W36rgLOBV5SVZMzip9ojbUB2NIafg1wCNjf7N8FbK2qnV01jNIsS48sW9HDXydJkjR/9D0YAn9J5waSI3SuK7wP+HpVfT3J9q6+75v80MwmQmfZ+bUAVTUOjLf6bAL2dAfBblW1DdgGsGTlOpebJUnSgtT3YFhV9wD3JLmqql7StfsltJaAp1oyTnLC0CdJkqTp6XswbHlsd0NVeRexJEnSaTJIwXCkuQaw2wOuCexyYI7qkSRJWlAGJhhW1dNmedxPnWD3dh74PERJkiRNYWCC4VyoqoMzPea81cuZ8N2VkiRpARqYB1xLkiSpvwyGkiRJAgyGkiRJahgMJUmSBBgMJUmS1DAYSpIkCTAYSpIkqWEwlCRJEmAwlCRJUsNgKEmSJGDAX4mX5MVV9Y6T9FkNrKyqiV585+59B1i7eawXQ0mSpBna62tp+2ogZgyTvDHJzc3fHUle1Ox6zhR9d3Y1rQMu7uqzozXe5N/dSc6co58gSZI07w3EjGFVvXryc5JrgJtO0H3xNMbb2N2WZAw4Mpv6JEmSFoKBmDGclOS5wJ1VdVer7WNNO0kCrE+yOMkFSV4HXDbd8auqelyyJEnS0BiIGcMki4CXA48Ermjvq6oLWpsbgC/QWWK+Bfgq8P3A6ml8zdFe1CpJkjSs+j5jmOShwJ8Ad1XVK6qqHeA+1+p3BvDLwNOBXwQOV9VfA//Y6rMhya7W398n+asku4BlTdsx1yNKkiSpo+8zhlX1VeCSJE9M8kG+dQ3hIuDN8M1Q+HZge1XdleTVwPVJLu0aaxwYn9xOsgnYU1XdN6wcI8koMAowsmxFL36WJEnSvNP3YNhyFfC8qtoHkGQp8OEknwCWArdU1Q6AqvqLJFcCPblmsKq2AdsAlqxc53WIkiRpQRqkYFgcG/QmP1dV3QnceUzn5rmFnftRJEmSdKoGKRheDryz9azBEeANVfWVPtYkSZK0YAxMMKyqzwAzftx5Ve0Cdh1n93bg8KyLkiRJWkAGJhjOhao6ONNjzlu9nAlfxyNJkhagvj+uRpIkSYPBYChJkiTAYChJkqSGwVCSJEmAwVCSJEkNg6EkSZIAg6EkSZIaBkNJkiQBBkNJkiQ1DIaSJEkCDIaSJElqDPS7kpO8uKrecTq/c/e+A6zdPHY6v1LSgNrre9MlLTADMWOY5I1Jbm7+7kjyombXc7r63TzFsTunaNvRGm/y7+4kZ87RT5AkSZr3BmLGsKpePfk5yTXATcfpunaKcHjuFONt7G5LMgYcOYUyJUmShtpABMNJSZ4L3FlVd7XaPga8par+CDgAXNN12Oh0x6+q6kmhkiRJQ2gggmGSRcDLgUcCV7T3VdUFrc0XAt3LwR+d5tccnXWBkiRJC0Dfg2GShwK/D7y7qn6ra/fnmj4bgC2t9kcAAb7Y7AfYSif8tfutAQ4B+5t+u4CtVXXMdYlJRmlmHkeWrTj1HyVJkjQP9T0YVtVXgUuSPDHJB4HFza5FwJubPuPA+OQxSS4Fzqiqq6cYst1vE7CnOwhOUcM2YBvAkpXrXG6WJEkLUt+DYctVwPOqah9AkqXAh5N8oqr2J1kBXN8+IMllwLqqWn3aq5UkSRoygxQMq/lrb3/zn1V1N3Bh90FTPa5GkiRJMzdIwfBy4J2tZw2OAG+oqq/0sSZJkqQFY2CCYVV9BpjNawZ+6QT7tgOHZ1WQJEnSAjMwwXC2qurvTrDv4EzHO2/1ciZ8DZYkSVqABuKVeJIkSeo/g6EkSZIAg6EkSZIaBkNJkiQBBkNJkiQ1DIaSJEkCDIaSJElqGAwlSZIEGAwlSZLUMBhKkiQJGIJX4vXa7n0HWLt5rN9lSNKCsNdXkEoDZaBnDJO8uN81SJIkLRQDMWOY5I3A9zebjwTeVFXbgecA72j1+wfgzq7D762qZ3SNtwNY2tXvfGBVVR3uYemSJElDYyCCYVW9evJzkmuAm47T9c6qunAa423sbksyBhyZZYmSJElDbyCC4aQkz6UT/u5qtX0MeEtV/RGwKMnNdGYDA3yt6fbsqrrnZONXVc1B2ZIkSUNhIIJhkkXAy+ksI1/R3ldVF7Q+P7XpfylwRlVdPYOvOXrqlUqSJA2vvgfDJA8Ffh94d1X9VtfuzzV9ngy8qNW+qNOcC1pt7wLOBra02tYAh4D9zTi7gK1VtbOrhlFgFGBk2YpT+0GSJEnzVN+DYVV9FbgkyROTfBBY3OxaBLy56XMbcFuS1cDLgCc0fT4LvK2q9rWGHJ/8kGQTsKc7CE5RwzZgG8CSletcbpYkSQtS34Nhy1XA8yZDXpKlwIeTfKKq9jd9rgOuBF7bbD8ZuB74odNdrCRJ0rAZpOcYVvPX3v7mP5OMAEuA26vqvqq6D/gUsDjJmae1UkmSpCE0SDOGlwPvbIW8EeANVfUVgKo6mmQL8IEk7eO2+GxCSZKkU5dhfoJLsxx9uKq+Md1j1q9fXxMTE3NYlSRJUm8kub2q1vdqvEGaMey5qjrY7xokSZLmi0G6xlCSJEl9ZDCUJEkSYDCUJElSw2AoSZIkwGAoSZKkhsFQkiRJgMFQkiRJDYOhJEmSAIOhJEmSGgZDSZIkAQP+SrwkL66qd5ykzzOq6sZefefufQdYu3msV8NJkjSw9m69pN8laMAMxIxhkjcmubn5uyPJi5pdz2n1uSrJ2ikOf+UU4+1ojTf5d3eSM+foJ0iSJM17AzFjWFWvnvyc5Brgppkcn2Q98PmqursZb+MUfcaAI6dWqSRJ0vAaiBnDSUmeC9xZVXe12j7WtE/V/ywgwHpgxcnGr6rqVa2SJEnDZiBmDJMsAl4OPBK4or2vqi5o+nwP8L+T3AdU83ddp0tdNY2vOdrToiVJkoZM34NhkocCvw+8u6p+q2v35yY/VNXrgNdNcfwjW583AFtau9cAh4D9zf5dwNaq2tk1xigwCjCy7KQTj5IkSUOp78Gwqr4KXJLkiUk+CCxudi0C3tzum+RdwKO6hlgGvLYZaxwYb/XfBOzpDoJT1LAN2AawZOU6l5slSdKC1Pdg2HIV8Lyq2geQZCnw4SSfqKr9TZ9VVXVR+6AkJwx9kiRJmp5Buvlk8rrB9jZdbZIkSZojgzRjeDnwztazBkeAN1TVV1p9zkxyc9dx552W6iRJkobcwATDqvoMcMJHsFfVj85w2O3A4dnWJEmStJAMTDCcC1V1cKbHnLd6ORO+IkiSJC1Ag3SNoSRJkvrIYChJkiTAYChJkqSGwVCSJEmAwVCSJEmNVPn86LYkXwPu6Hcd89TDgS/3u4h5zPM3e5672fPczZ7nbvY8d6emff7OraoVvRp4qB9XM0t3VNX6fhcxHyWZ8NzNnudv9jx3s+e5mz3P3ex57k7NXJ4/l5IlSZIEGAwlSZLUMBg+0LZ+FzCPee5Ojedv9jx3s+e5mz3P3ex57k7NnJ0/bz6RJEkS4IyhJEmSGgbDliT/NcmtST6e5An9rqcfkqxI8oYk/7XZ/s4ktzTn5E2tfg84V73oO58leWiSa5LsSvJ/kjza8zc9SRYn+ZPm3N2aZLXnbuaSfCrJxZ676Uuyu/n3bleSF3rupi/JDzT/XffxJL/quZu+JC9r/Xu3K8mXB+b8VZV/neX0Hwa2NZ+/G/hQv2vq03n438BrgK3N9o3A2ubz9cAPHu9cnWrffv/2Hpy7VcCq5vMlwO94/qZ97hYBD24+Xwpc6bmb8Tn8SeBzwMWeuxmdt5u7tj130ztvZwIfBM7x3J3yuXwe8KpBOX8+x/Bbfgz4A4Cq+uskD+tzPX1RVT+X5ELg4iRnAGdV1d5m9x8CTwG+ja5z1aO+n5jbXze3quqfWptfAb6B529aqup+4FCzuQ6YADZ47qYnyUOAnwV+n87zaf33bvrun/zgf+fNyDOAzwN/kORM4NV47mYsySLgPwE/AVwyCOfPpeRv+Xbg7tb2keb/YAvZCuBfWtv/ApzDFOcKeEQP+g6FJKvp/H9/b8bzN21Jrkjyd8B64FN47mbifwKvpxNyHoLnblqSnA08plkOvQ5YieduutYBDwOeCfxH4Fo8d7PxbGCcAfrPrTOG33KAY0/W/c0sxkL2VeChre1z6PxL9yC6zhWwvwd9570kzwSeBfwinRmwh7Z2e/5OoKreBLwpyTOAt+C5m5YkPwPcWVV/keQS/M/ttFXVPcBjAJJswH/vZuII8OGqOgLsTbKfY3+35256/gOdYP01BuTfvYU+I9b2UTrX6JDku4Av9Lec/quqe4ElzQwYwHOBW5jiXPWo77yW5HuAZ1XVi6vqXzx/05fkIUnSbN4JjOC5m64XAt+V5Bo6v/fXgCd47k4uyUhr826g8N+76fpzOsvJJHkEnWCz2HM3fUm+jc4y75cG6X8vnDH8ljHgx5N8lM6/4C/ucz2D4hXADUm+AfxxVf1tkjuY+lydUt/T+aPmyMXADyfZ1Wzfiedvuh4HvLX5PfcCL6PzknjP3UlU1SWTn5O8DriNznKR5+7kHpvkXcB9zd/ldK7T8tydRFV9MskdST5OZ/bwFXQmmzx30/dUOgF70kD874UPuJYkSRLgUrIkSZIaBkNJkiQBBkNJkiQ1DIaSJEkCDIaSJElqGAwlSZIEGAwlSZLUMBhKkiQJgP8Hs+dM4juqnbEAAAAASUVORK5CYII=",
      "text/plain": [
       "<Figure size 720x720 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "data_result['인구수'].plot(kind='barh', figsize=(10, 10))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "---"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 219,
   "metadata": {},
   "outputs": [],
   "source": [
    "import matplotlib.pyplot as plt\n",
    "# import matplotlib as apl\n",
    "\n",
    "plt.rcParams['axes.unicode_minus'] = False # 마이너스 부호 때문에 한글이 깨질 수 가 있어 주는 설정\n",
    "rc('font', family='Malgun Gothic')\n",
    "# %matplotlib inline\n",
    "get_ipython().run_line_magic('matplotlib', 'inline')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 221,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>소계</th>\n",
       "      <th>최근증가율</th>\n",
       "      <th>인구수</th>\n",
       "      <th>한국인</th>\n",
       "      <th>외국인</th>\n",
       "      <th>고령자</th>\n",
       "      <th>외국인비율</th>\n",
       "      <th>고령자비율</th>\n",
       "      <th>CCTV비율</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>구별</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>강남구</th>\n",
       "      <td>3238</td>\n",
       "      <td>150.619195</td>\n",
       "      <td>561052</td>\n",
       "      <td>556164</td>\n",
       "      <td>4888</td>\n",
       "      <td>65060</td>\n",
       "      <td>0.871220</td>\n",
       "      <td>11.596073</td>\n",
       "      <td>0.577130</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>강동구</th>\n",
       "      <td>1010</td>\n",
       "      <td>166.490765</td>\n",
       "      <td>440359</td>\n",
       "      <td>436223</td>\n",
       "      <td>4136</td>\n",
       "      <td>56161</td>\n",
       "      <td>0.939234</td>\n",
       "      <td>12.753458</td>\n",
       "      <td>0.229358</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>강북구</th>\n",
       "      <td>831</td>\n",
       "      <td>125.203252</td>\n",
       "      <td>328002</td>\n",
       "      <td>324479</td>\n",
       "      <td>3523</td>\n",
       "      <td>56530</td>\n",
       "      <td>1.074079</td>\n",
       "      <td>17.234651</td>\n",
       "      <td>0.253352</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>강서구</th>\n",
       "      <td>911</td>\n",
       "      <td>134.793814</td>\n",
       "      <td>608255</td>\n",
       "      <td>601691</td>\n",
       "      <td>6564</td>\n",
       "      <td>76032</td>\n",
       "      <td>1.079153</td>\n",
       "      <td>12.500021</td>\n",
       "      <td>0.149773</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>관악구</th>\n",
       "      <td>2109</td>\n",
       "      <td>149.290780</td>\n",
       "      <td>520929</td>\n",
       "      <td>503297</td>\n",
       "      <td>17632</td>\n",
       "      <td>70046</td>\n",
       "      <td>3.384722</td>\n",
       "      <td>13.446362</td>\n",
       "      <td>0.404854</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "       소계       최근증가율     인구수     한국인    외국인    고령자     외국인비율      고령자비율  \\\n",
       "구별                                                                         \n",
       "강남구  3238  150.619195  561052  556164   4888  65060  0.871220  11.596073   \n",
       "강동구  1010  166.490765  440359  436223   4136  56161  0.939234  12.753458   \n",
       "강북구   831  125.203252  328002  324479   3523  56530  1.074079  17.234651   \n",
       "강서구   911  134.793814  608255  601691   6564  76032  1.079153  12.500021   \n",
       "관악구  2109  149.290780  520929  503297  17632  70046  3.384722  13.446362   \n",
       "\n",
       "       CCTV비율  \n",
       "구별             \n",
       "강남구  0.577130  \n",
       "강동구  0.229358  \n",
       "강북구  0.253352  \n",
       "강서구  0.149773  \n",
       "관악구  0.404854  "
      ]
     },
     "execution_count": 221,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data_result.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 소계 컬럼 시각화"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 224,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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",
      "text/plain": [
       "<Figure size 720x720 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "data_result['소계'].plot(kind='barh', grid=True, figsize=(10,10));"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "; 세미콜론을 찍으면 깔끔하게 그래프만 출력된다."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 229,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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",
      "text/plain": [
       "<Figure size 720x720 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "def drawGraph():\n",
    "    data_result['소계'].sort_values().plot(\n",
    "        kind='barh', grid=True, title='가장 CCTV가 많은 구', figsize=(10,10));\n",
    "drawGraph()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 230,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>소계</th>\n",
       "      <th>최근증가율</th>\n",
       "      <th>인구수</th>\n",
       "      <th>한국인</th>\n",
       "      <th>외국인</th>\n",
       "      <th>고령자</th>\n",
       "      <th>외국인비율</th>\n",
       "      <th>고령자비율</th>\n",
       "      <th>CCTV비율</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>구별</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>강남구</th>\n",
       "      <td>3238</td>\n",
       "      <td>150.619195</td>\n",
       "      <td>561052</td>\n",
       "      <td>556164</td>\n",
       "      <td>4888</td>\n",
       "      <td>65060</td>\n",
       "      <td>0.871220</td>\n",
       "      <td>11.596073</td>\n",
       "      <td>0.577130</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>강동구</th>\n",
       "      <td>1010</td>\n",
       "      <td>166.490765</td>\n",
       "      <td>440359</td>\n",
       "      <td>436223</td>\n",
       "      <td>4136</td>\n",
       "      <td>56161</td>\n",
       "      <td>0.939234</td>\n",
       "      <td>12.753458</td>\n",
       "      <td>0.229358</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>강북구</th>\n",
       "      <td>831</td>\n",
       "      <td>125.203252</td>\n",
       "      <td>328002</td>\n",
       "      <td>324479</td>\n",
       "      <td>3523</td>\n",
       "      <td>56530</td>\n",
       "      <td>1.074079</td>\n",
       "      <td>17.234651</td>\n",
       "      <td>0.253352</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>강서구</th>\n",
       "      <td>911</td>\n",
       "      <td>134.793814</td>\n",
       "      <td>608255</td>\n",
       "      <td>601691</td>\n",
       "      <td>6564</td>\n",
       "      <td>76032</td>\n",
       "      <td>1.079153</td>\n",
       "      <td>12.500021</td>\n",
       "      <td>0.149773</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>관악구</th>\n",
       "      <td>2109</td>\n",
       "      <td>149.290780</td>\n",
       "      <td>520929</td>\n",
       "      <td>503297</td>\n",
       "      <td>17632</td>\n",
       "      <td>70046</td>\n",
       "      <td>3.384722</td>\n",
       "      <td>13.446362</td>\n",
       "      <td>0.404854</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "       소계       최근증가율     인구수     한국인    외국인    고령자     외국인비율      고령자비율  \\\n",
       "구별                                                                         \n",
       "강남구  3238  150.619195  561052  556164   4888  65060  0.871220  11.596073   \n",
       "강동구  1010  166.490765  440359  436223   4136  56161  0.939234  12.753458   \n",
       "강북구   831  125.203252  328002  324479   3523  56530  1.074079  17.234651   \n",
       "강서구   911  134.793814  608255  601691   6564  76032  1.079153  12.500021   \n",
       "관악구  2109  149.290780  520929  503297  17632  70046  3.384722  13.446362   \n",
       "\n",
       "       CCTV비율  \n",
       "구별             \n",
       "강남구  0.577130  \n",
       "강동구  0.229358  \n",
       "강북구  0.253352  \n",
       "강서구  0.149773  \n",
       "관악구  0.404854  "
      ]
     },
     "execution_count": 230,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data_result.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 231,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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",
      "text/plain": [
       "<Figure size 720x720 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "def drawGraph():\n",
    "    data_result['CCTV비율'].sort_values().plot(\n",
    "        kind='barh', grid=True, title='가장 CCTV가 많은 구', figsize=(10,10));\n",
    "drawGraph()\n",
    "# Data Frame Plot 검색하면 더 자세한 데이터 설명을 알 수 있다."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 6. 데이터의 경향 표시"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 232,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>소계</th>\n",
       "      <th>최근증가율</th>\n",
       "      <th>인구수</th>\n",
       "      <th>한국인</th>\n",
       "      <th>외국인</th>\n",
       "      <th>고령자</th>\n",
       "      <th>외국인비율</th>\n",
       "      <th>고령자비율</th>\n",
       "      <th>CCTV비율</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>구별</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>강남구</th>\n",
       "      <td>3238</td>\n",
       "      <td>150.619195</td>\n",
       "      <td>561052</td>\n",
       "      <td>556164</td>\n",
       "      <td>4888</td>\n",
       "      <td>65060</td>\n",
       "      <td>0.871220</td>\n",
       "      <td>11.596073</td>\n",
       "      <td>0.577130</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>강동구</th>\n",
       "      <td>1010</td>\n",
       "      <td>166.490765</td>\n",
       "      <td>440359</td>\n",
       "      <td>436223</td>\n",
       "      <td>4136</td>\n",
       "      <td>56161</td>\n",
       "      <td>0.939234</td>\n",
       "      <td>12.753458</td>\n",
       "      <td>0.229358</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>강북구</th>\n",
       "      <td>831</td>\n",
       "      <td>125.203252</td>\n",
       "      <td>328002</td>\n",
       "      <td>324479</td>\n",
       "      <td>3523</td>\n",
       "      <td>56530</td>\n",
       "      <td>1.074079</td>\n",
       "      <td>17.234651</td>\n",
       "      <td>0.253352</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>강서구</th>\n",
       "      <td>911</td>\n",
       "      <td>134.793814</td>\n",
       "      <td>608255</td>\n",
       "      <td>601691</td>\n",
       "      <td>6564</td>\n",
       "      <td>76032</td>\n",
       "      <td>1.079153</td>\n",
       "      <td>12.500021</td>\n",
       "      <td>0.149773</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>관악구</th>\n",
       "      <td>2109</td>\n",
       "      <td>149.290780</td>\n",
       "      <td>520929</td>\n",
       "      <td>503297</td>\n",
       "      <td>17632</td>\n",
       "      <td>70046</td>\n",
       "      <td>3.384722</td>\n",
       "      <td>13.446362</td>\n",
       "      <td>0.404854</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "       소계       최근증가율     인구수     한국인    외국인    고령자     외국인비율      고령자비율  \\\n",
       "구별                                                                         \n",
       "강남구  3238  150.619195  561052  556164   4888  65060  0.871220  11.596073   \n",
       "강동구  1010  166.490765  440359  436223   4136  56161  0.939234  12.753458   \n",
       "강북구   831  125.203252  328002  324479   3523  56530  1.074079  17.234651   \n",
       "강서구   911  134.793814  608255  601691   6564  76032  1.079153  12.500021   \n",
       "관악구  2109  149.290780  520929  503297  17632  70046  3.384722  13.446362   \n",
       "\n",
       "       CCTV비율  \n",
       "구별             \n",
       "강남구  0.577130  \n",
       "강동구  0.229358  \n",
       "강북구  0.253352  \n",
       "강서구  0.149773  \n",
       "관악구  0.404854  "
      ]
     },
     "execution_count": 232,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data_result.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 인구수와 소계 컬럼으로 scatter plot 그리기"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 234,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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",
      "text/plain": [
       "<Figure size 1008x720 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "def drawGraph():\n",
    "    \n",
    "    plt.figure(figsize=(14,10))\n",
    "    plt.scatter(data_result['인구수'], data_result['소계'], s=50)\n",
    "    plt.xlabel('인구수')\n",
    "    plt.ylabel(\"CCTV\")\n",
    "    plt.grid(True)\n",
    "    plt.show()\n",
    "\n",
    "drawGraph()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Numpy를 이용한 1차 직선 만들기\n",
    "- np.polyfit(): 직선을 구성하기 위한 계수를 계산\n",
    "- np.poly1d(): polyfit 으로 찾은 계수로 파이썬에서 사용할 수 있는 함수로 만들어주는 기능"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 235,
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 236,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([1.38596837e-03, 9.35804531e+02])"
      ]
     },
     "execution_count": 236,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "fp1 = np.polyfit(data_result['인구수'], data_result['소계'], 1)\n",
    "fp1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 237,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "poly1d([1.38596837e-03, 9.35804531e+02])"
      ]
     },
     "execution_count": 237,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "f1 = np.poly1d(fp1)\n",
    "f1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 238,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1490.191879351763"
      ]
     },
     "execution_count": 238,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "f1(400000)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "- 인구가 40만인 구에서 서울시의 전체 경향에 맞는 적당한 CCTV 수는?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 239,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([100000.        , 106060.60606061, 112121.21212121, 118181.81818182,\n",
       "       124242.42424242, 130303.03030303, 136363.63636364, 142424.24242424,\n",
       "       148484.84848485, 154545.45454545, 160606.06060606, 166666.66666667,\n",
       "       172727.27272727, 178787.87878788, 184848.48484848, 190909.09090909,\n",
       "       196969.6969697 , 203030.3030303 , 209090.90909091, 215151.51515152,\n",
       "       221212.12121212, 227272.72727273, 233333.33333333, 239393.93939394,\n",
       "       245454.54545455, 251515.15151515, 257575.75757576, 263636.36363636,\n",
       "       269696.96969697, 275757.57575758, 281818.18181818, 287878.78787879,\n",
       "       293939.39393939, 300000.        , 306060.60606061, 312121.21212121,\n",
       "       318181.81818182, 324242.42424242, 330303.03030303, 336363.63636364,\n",
       "       342424.24242424, 348484.84848485, 354545.45454545, 360606.06060606,\n",
       "       366666.66666667, 372727.27272727, 378787.87878788, 384848.48484848,\n",
       "       390909.09090909, 396969.6969697 , 403030.3030303 , 409090.90909091,\n",
       "       415151.51515152, 421212.12121212, 427272.72727273, 433333.33333333,\n",
       "       439393.93939394, 445454.54545455, 451515.15151515, 457575.75757576,\n",
       "       463636.36363636, 469696.96969697, 475757.57575758, 481818.18181818,\n",
       "       487878.78787879, 493939.39393939, 500000.        , 506060.60606061,\n",
       "       512121.21212121, 518181.81818182, 524242.42424242, 530303.03030303,\n",
       "       536363.63636364, 542424.24242424, 548484.84848485, 554545.45454545,\n",
       "       560606.06060606, 566666.66666667, 572727.27272727, 578787.87878788,\n",
       "       584848.48484848, 590909.09090909, 596969.6969697 , 603030.3030303 ,\n",
       "       609090.90909091, 615151.51515152, 621212.12121212, 627272.72727273,\n",
       "       633333.33333333, 639393.93939394, 645454.54545455, 651515.15151515,\n",
       "       657575.75757576, 663636.36363636, 669696.96969697, 675757.57575758,\n",
       "       681818.18181818, 687878.78787879, 693939.39393939, 700000.        ])"
      ]
     },
     "execution_count": 239,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "fx = np.linspace(100000, 700000, 100)\n",
    "fx"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "- 경향선을 그리기 위한 X 데이터 생성  \n",
    "- np.linspace(a,b,n): a부터 b까지 n개의 등간격 데이터 생성"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 240,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAA0UAAAJMCAYAAAA1/w3JAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjUuMCwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy8/fFQqAAAACXBIWXMAAAsTAAALEwEAmpwYAABJD0lEQVR4nO3de1Rc1333/89mYEADkhAgISFpmNi62LIlfAFkXWYsJ7Lj2DhNEzeO0ziVmhU77pNmpW6SNuovdftT21z8tHHS5lI/TaU+edo4Fzexg93+kng9mBGSheSLLtYlTmwYSegG6AZIIIb9+4PRMQMDujEzzJz3ay3Wgn32oO94mxk+nLO/x1hrBQAAAABulZPuAgAAAAAgnQhFAAAAAFyNUAQAAADA1QhFAAAAAFyNUAQAAADA1QhFAAAAAFwtN90FjIeysjIbCATSXYaju7tbhYWF6S4D44x1zU6sa/ZibbMT65q9WNvsNJHW9ZVXXmm31k5PdCwrQlEgEND27dvTXYajoaFBq1atSncZGGesa3ZiXbMXa5udWNfsxdpmp4m0rsaY1tGOcfkcAAAAAFcjFAEAAABwNUIRAAAAAFcjFAEAAABwNUIRAAAAAFcjFAEAAABwNUIRAAAAAFcjFAEAAABwNUIRAAAAAFcjFAEAAABwNUIRAAAAAFcjFAEAAABwNUIRAAAAAFcjFAEAAABwNUIRAAAAAFcjFAEAAABwNUIRAAAAAFcjFAEAAABwNUIRAAAAAFfLTXcBAAAAuDpdvf2q39Gmlo5uBUoLVVdVoaJ8fs0DLhU/LQAAABlsW0un1mxolrVST19UPq9H65/fo41ra1UTKEl3eUBG4PI5AACADNXV2681G5rV3RtVT19U0mAw6u6Nxsb701whkBkIRQAAABmqfkebrE18zFqpfmdbagsCMhShCAAAIEO1dHQ7Z4iG6+mLqqW9J8UVAZmJUAQAAJChAqWF8nk9CY/5vB4FynwprgjITIQiAACADFVXVSFjEh8zRqpbUpHagoAMRSgCAADIUEX5udq4tlaF+R7njJHP61Fhvic2TqNh4FLwkwIAAJDBagIlal63WvU729TS3qNAmU91SyoIRMBl4KcFAAAgwxXm5+qBGn+6ywAyFpfPAQAAAHA1QhEAAAAAVyMUAQAAAHA1QhEAAAAAVyMUAQAAAHA1QhEAAAAAVyMUAQAAAHA1QhEAAAAAVyMUAQAAAHA1QhEAAAAAVyMUAQAAAHA1QhEAAAAAVyMUAQAAAHA1QhEAAAAAVyMUAQAAAHA1QhEAAAAAVyMUAQAAAHA1QhEAAAAAVyMUAQAAAHA1QhEAAAAAVyMUAQAAAHA1QhEAAAAAVyMUAQAAAHA1QhEAAAAAVyMUAQAAAHA1QhEAAAAAVyMUAQAAAHA1QhEAAAAAVyMUAQAAAHA1QhEAAAAAVyMUAQAAAHA1QhEAAAAAVyMUAQAAAHA1QhEAAAAAVyMUAQAAAHA1QhEAAAAAVyMUAQAAAHA1QhEAAAAAVyMUAQAAAHC1pIQiY4zXGPNzY0yDMeYlY8xsY8xCY8yLxpgmY8wTQ+auj81pMsbcEBtLOBcAAAAAxltukr5vv6QHrLU9xpiPSfoDSUFJn7DWthhjfmyMWSrJK6ncWnu7MeZGSU9IukfSk8PnWmu3JqlWAAAAAC6WlDNF1toBa21P7Mv5knZJKrDWtsTGnpG0TNJdkn4Qe8xuSSXGmNxR5gIAAADAuEvaniJjzOeNMW9Kqpb0qqSOIYc7JE2TNEPS8SHj/ZLKR5kLAAAAAOPOWGuT+w8Y8z5JaySVWmtXx8Y+rMFA5Jf0c2ttODbeKOm9sbG4udbafxr2fR+W9LAklZeX3/r0008n9Xlcjq6uLhUVFaW7DIwz1jU7sa7Zi7XNTqxr9mJts9NEWtc77rjjFWttdaJjSdlTZIyZLKnLDiauiCSPpHxjzGxr7SFJH5T015LmSbpfUtgYs0jSQWvtWWNMorlxrLVPSXpKkqqrq+2qVauS8VSuSENDgyZSPRgfrGt2Yl2zF2ubnVjX7MXaZqdMWddkNVq4TtKTxpheSWclfVpSmaSfxMaes9buNcbsl3SPMSYs6YykR2KPf2z43CTVCQAAAMDlkhKKrLXbJK0YNvy2hjVMsNYOSHp0lMfTXAEAAABA0nHzVgAAAACuRigCAAAA4GqEIgAAAACuRigCAAAA4GqEIgAAAACuRigCAAAA4GqEIgAAAACuRigCAAAA4GqEIgAAAACuRigCAAAA4GqEIgAAAACuRigCAAAA4GqEIgAAAACuRigCAAAA4GqEIgAAAACuRigCAAAA4GqEIgAAAACuRigCAAAA4GqEIgAAAACuRigCAAAA4GqEIgAAAACuRigCAAAA4GqEIgAAAACuRigCAAAA4GqEIgAAAACuRigCAAAA4GqEIgAAAACuRigCAAAA4GqEIgAAAACuRigCAAAA4GqEIgAAAACuRigCAAAA4GqEIgAAAACuRigCAAAA4GqEIgAAAACuRigCAAAA4GqEIgAAAACuRigCAAAA4GqEIgAAAACuRigCAAAA4GqEIgAAAACuRigCAAAA4GqEIgAAAACuRigCAAAA4GqEIgAAAACuRigCAAAA4GqEIgAAAACuRigCAAAA4GqEIgAAAACuRigCAAAA4GqEIgAAAACuRigCAAAA4GqEIgAAAACuRigCAAAA4GqEIgAAAACuRigCAAAA4GqEIgAAAACuRigCAAAA4GqEIgAAAACuRigCAAAA4GqEIgAAAACuRigCAAAA4GqEIgAAAACuRigCAAAA4GqEIgAAAACuRigCAAAA4GqEIgAAAACuRigCAAAA4GqEIgAAAACuRigCAAAA4GqEIgAAAACuRigCAAAA4GqEIgAAAACuRigCAAAA4GqEIgAAAACuRigCAAAA4GqEIgAAAACuRigCAAAA4GqEIgAAAACuRigCAAAA4GqEIgAAAACuRigCAAAA4GqEIgAAAACuRigCAAAA4GqEIgAAAACuRigCAAAA4GqEIgAAAACuRigCAAAA4GqEIgAAAACuRigCAAAA4GqEIgAAAACuRigCAAAA4GqEIgAAAACuRigCAAAA4GqEIgAAAACulpRQZIwpNsY8bYxpMMY0GmPeZYx5yBizJzb2iyFz1xtjXjLGNBljboiNLTTGvBgbeyIZNQIAAACAJOUm6fv6JD1mrW0zxtwr6XOS9kn6orX22QuTjDFBSeXW2tuNMTdKekLSPZKelPQJa22LMebHxpil1tqtSaoVAAAAgIsl5UyRtbbNWtsW+/KEpG5JxbHPh7pL0g9ij9ktqcQYkyupwFrbEpvzjKRlyagTAAAAAJJ1pkiSZIyZrcGzRJ+W9Iikrxljzkv6vrX2KUkzJB0f8pB+SeWSOoaMdUi6PsH3fljSw5JUXl6uhoaGZDyFK9LV1TWh6sH4YF2zE+uavVjb5Bmw0qmzfertH1B+bo6mTvIqx6Tm32Zdsxdrm50yZV2TFoqMMXWS7pP0SWtth6THJT1ujPFJetYY0yTplKRpQx42IKlTg2eVLpim+OAkSYqFqqckqbq62q5atSoJz+LKNDQ0aCLVg/HBumYn1jV7sbbJsa2lU2s2NMtaqacvKp9XMuacNq6tVU2gJOn/PuuavVjb7JQp65qsRgtLJN1nrX0kFogUuyxOks5KOiPJSgpLuj92fJGkg9bas5LyY2eZJOmDkl5MRp0AAODSdfX2a82GZnX3RtXTF5U0GIy6e6Ox8f40VwgAVyZZZ4rulhQ0xjTEvo5IOmqMqY39mz+11u4xxuyTdI8xJqzBoPRIbP5jkn5ijOmV9Jy1dm+S6gQAAJeofkebrE18zFqpfmebHqjxp7YoABgHSQlF1tqvSfraJcwbkPRogvFtorkCAAATSktHt3OGaLievqha2ntSXBEAjA9u3goAAC5JoLRQPq8n4TGf16NAmS/FFQHA+CAUAQCAS1JXVSEzSpc5Y6S6JRWpLQgAxgmhCAAAXJKi/FxtXFurwnyPc8bI5/WoMN8TG0/qnT4AIGl49QIAAJesJlCi5nWrVb+zTS3tPQqU+VS3pIJABCCj8QoGAAAuS2F+Ll3mAGQVLp8DAAAA4GqEIgAAAACuRigCAAAA4GqEIgAAAACuRigCAAAA4GqEIgAAAACuRigCAAAA4GqEIgAAAACuRigCAAAA4GqEIgAAAACuRigCAAAA4GqEIgAAAACuRigCAAAA4GqEIgAAAACuRigCAAAA4GqEIgAAAACuRigCAAAA4GqEIgAAAACuRigCAAAA4GqEIgAAAACuRigCAAAA4GqEIgAAAACuRigCAAAA4GqEIgAAAACuRigCAAAA4GqEIgAAAACuRigCAAAA4GqEIgAAAACulpvuAgAAwMV19farfkebWjq6FSgtVF1VhYryeRsHgPHAqykAABPctpZOrdnQLGulnr6ofF6P1j+/RxvX1qomUJLu8gAg43H5HAAAE1hXb7/WbGhWd29UPX1RSYPBqLs3GhvvT3OFAJD5CEUAAExg9TvaZG3iY9ZK9TvbUlsQAGQhQhEAABNYS0e3c4ZouJ6+qFrae1JcEQBkH0IRAAATWKC0UD6vJ+Exn9ejQJkvxRUBQPYhFAEAMIHVVVXImMTHjJHqllSktiAAyEKEIgAAJrCi/FxtXFurwnyPc8bI5/WoMN8TG6eRLABcLV5JAQCY4GoCJWpet1r1O9vU0t6jQJlPdUsqCEQAME54NQUAIAMU5ufqgRp/ussAgKzE5XMAAAAAXI1QBAAAAMDVCEUAAAAAXI1QBAAAAMDVCEUAAAAAXI1QBAAAAMDVCEUAAAAAXI1QBAAAAMDVCEUAAAAAXI1QBAAAAMDVCEUAAAAAXI1QBAAAAMDVCEUAAAAAXI1QBAAAAMDVCEUAAAAAXI1QBAAAAMDVCEUAAAAAXI1QBAAAAMDVCEUAAAAAXI1QBAAAAMDVCEUAAAAAXI1QBAAAAMDVCEUAAAAAXI1QBAAAAMDVCEUAAAAAXI1QBAAAAMDVCEUAAAAAXI1QBAAAAMDVctNdAAAAcK+u3n7V72hTS0e3AqWFqquqUFF+en49mUi1AEgtftIBAEBabGvp1JoNzbJW6umLyuf1aP3ze7Rxba1qAiWurQVA6nH5HAAASLmu3n6t2dCs7t6oevqikgbDSHdvNDbe78paAKQHoQhwoa7efj3dHNFX/muvnm6OqIs3fAApVr+jTdYmPmatVL+zzZW1AEgPLp8DXIZLRABMBC0d3c5ZmeF6+qJqae9xZS0A0oMzRYCLcIkIgIkiUFoon9eT8JjP61GgzOfKWgCkB6EIcBEuEQEwUdRVVciYxMeMkeqWVLiyFgDpQSgCXIRLRABMFEX5udq4tlaF+R7nLI3P61Fhvic2nror/CdSLQDSg59ywEUuXCKSKBhxiQiAVKsJlKh53WrV72xTS3uPAmU+1S2pSEsImUi1AEi9MX/SjTEl1trOVBUDILnqqiq0/vk9CY9xiQiAdCjMz9UDNf50lyFpYtUCILUudvncz40xPzLGvM+Y0a62BZApuEQEAABgpDF/A7LWrjDGXC/pDyT9lTHmRUkbrLVvpqQ6AOOOS0QAAADiXfS3IGvtXkl/HjtTtFrS48aYCmvtu5NeHYCk4BIRAACAd1xO97mVkj4s6VpJ/19yygEAAACA1LpYo4WFkj4u6V5JWyR9z1r7cioKAwAAAIBUuNjlc09K2ijp/7XW9ia9GgAAAABIsYuFohettT9MSSUAAAAAkAYX21N0T0qqAAAAAIA0udiZomuNMX+X6IC1dl0S6gEAAACAlLpYKOqU9N+SuHErAAAAgKx0sVB00lrbmJJKAAAAACANLran6P9JSRUAAAAAkCYXC0VfNMbkDR0wxviMMRuTVxIAAAAApM7FQtFka+35oQPW2h5Jc8Z6kDGm2BjztDGmwRjTaIx5lzFmoTHmRWNMkzHmiSFz1xtjXoqN3xAbSzgXAAAAAMbbxfYU5Y8ynjfK+AU+SY9Za9uMMfdK+pykayR9wlrbYoz5sTFmqSSvpHJr7e3GmBslPaHBNuBPDp9rrd16qU8KAAAAAC7Vxc4UbTXG/N7QAWNMSNKhsR5krW2z1rbFvjwhqVdSgbW2JTb2jKRlku6S9IPYY3ZLKjHG5I4yFwAAAADGnbHWjn7QGJ+kH0rqkPS6pHmSbpb0IWvtkYt+c2NmS/pHSX8s6RvW2vtj43dKWilppqR/jAUiGWM2SXog0Vxr7ePDvvfDkh6WpPLy8luffvrpS3/WSdbV1aWioqJ0l4FxxrpmJ9Y1e7G22Yl1zV6sbXaaSOt6xx13vGKtrU507GKXz31T0ockLZY0X1KzpHWxjz8f64HGmDpJ90n6pKQeScVDDk+TdFzSpNjnFwxo8N5IiebGsdY+JekpSaqurrarVq26yFNJnYaGBk2kejA+WNfsxLpmL9Y2O7Gu2Yu1zU6Zsq4Xu3xuvrW2z1r7irX2aWvtZmvtaUkJE9YFxpglku6z1j5ire2w1p6VlB87cyRJH5T0oqSwpAtnhBZJOjjGXAAAAAAYdxc7U+S9wsfdLSlojGmIfR2R9JiknxhjeiU9Z63da4zZL+keY0xY0hlJj8Tmj5h7kX8PAAAAAK7IxcLNfmNM0FobvjAQa5t9aqwHWWu/JulrCQ4tGzZvQNKjCR6/bfhcAAAAAEiGi4Wiz0n6mTHmV3qn0cKDkj6S5LoAAAAAICXG3FNkrW2XtErSLknXSWqTtMpa+2bySwMAAACA5LvYmSJZa/s1eK8gAAAAAMg6F+s+BwAAAABZjVAEAAAAwNUIRQAAAABcjVAEAAAAwNUIRQAAAABcjVAEAAAAwNUIRQAAAABcjVAEAAAAwNUIRQAAAABcjVAEAAAAwNUIRQAAAABcLTfdBQAAAADITJ1nO7UpskmNrY1qOtCkXz30KxV6C9Nd1mUjFAEAMMF09farfkebWjq6FSgtVF1VhYryecsGkH4HTx9UuDWsxtZGhSNhvXH8jbjjWw9t1bvf9e40VXfleIUFAGAC2dbSqTUbmmWt1NMXlc/r0frn92jj2lrVBErSXR4AF/rh7h/qhd+8oMbWRrWcbBlzbrg1TCgCAABXrqu3X2s2NKu7N+qM9fQNfr5mQ7Oa161WIWeMACRJdCCqM31nVFxQHDf+wzd+qJ/u+2nCx+Tm5OqWWbco5A8pVBnSSv/KFFQ6/nhlBQBcFi7tSp76HW2yNvExa6X6nW16oMaf2qIAZK3e/l5tb9vuXArXdKBJH7juA/q3D/xb3LygP+iEokm5k3TbnNsUqgwp6A/qtjm3ZeQeouF4FwMAXDIu7Uqulo5u58zQcD19UbW096S4IgDZpKuvS1sObHFC0NZDW3Wu/1zcnHBreMTj7l1wr84PnFeoMqRbZt0ir8ebqpJThlAEALgkXNqVfIHSQvm8noTByOf1KFDmS0NVADLdG8fe0Jpn1+i1w68pahP/4eWCc/3ndPLcybhL6BaULtAXVnwhyVWmF/cpAgBckku5tAtXp66qQsYkPmaMVLekIrUFAcgoB04d0H/s+o8RZ39mFs3U9rbtCQPRvJJ5WnvTWv3r+/9Vv/nj3+jQY4dG7ClyA/6kBwC4JFzalXxF+bnauLZ2xCWKxkgb19ZyJg6Aw1qrX3f82rkULhwJO53hwmvDcQ0PSn2lWjR9kfYe36vF5YsV8ocUrAwq6A9q1uRZaXoGEwuvrgCAS8KlXalREyhR87rVqt/Zppb2HgXKfKpbUkEgAlwuOhDVjqM7FG4NOyHoWPexhHMbWxtHdIF7+kNPa86UOZo2aVoqys04vMICAC5JXVWF1j+/J+ExLu0aX4X5uXSZAxDnI898RD/Z85Mx5/jyfFo2Z5kCxYERxxaXL05SZdmBUAQAuCRc2gUAyXOm94w2H9iscCSsaQXT9KfL/zTueE1FzYhQNK1gmnMZXKgypJtn3qw8T14qy84avIMBAC4Zl3YBwPg43n188DK42OVwrx15TQN2QJK0sHThiFAU9AdVMbnCuT9QqDKkRdMXKcfQN2088C4GALgsXNoFAJfvTO8ZPbv/WYVbw2qMNGpf+75R5+7v2K+jXUdVXlTujN025zYd/JODMqO1qMRVIRQBAAAA48haKysbdxanq69LD/30oVEfY2RUNbNKQf/g5XBF3qL444ShpCIUAQAAAFehf6BfO47scNpjb4ps0s8f/LmWzlnqzJk1eZbml8zXm51vSpLycvJUM7vGuRRu+dzlrrw/0ERBKAIAAAAuw7n+c2o+1OzsB2o60KSuvq64OeFIOC4USdKj1Y+qq69Lwcqgls5eqkl5k1JZNsZAKAIAAAAuwb+9/m/63mvf09ZDW9UX7Rtz7va27SPG/mTZnySrNFwlQhEAAAAwxLHuY2o706abZt4UNx45FVE4Ek74mNmTZ8d1hrt++vUpqBTjhVAEAAAAV2s92ersB2psbdT+jv1aPGOxdj66M25eqDLkfL6gdIFC/pBzn6BAcYBmCBmMUAQAAADXsNZqb/tepzV2uDWsA6cPjJi3+9hudZ7tVMmkEmesdnatfvx7P1bQH4xrl43MRygCAACAK3Se7dTCf1qo9p72Med5PV7VVNToWPexuFA0KW+S7l90f7LLRBoQigAAAJA1zp4/O9gZLhLWh2/4sBaULnCOlUwqkS/PN+IxhXmFWj53ubMnqHZ2LZ3hXIZQBAAAgIx16twpbT6w2dkPtK1tm9MZbkr+lLhQJA3uC/qvN//L2QsUqgzpppk3KTeHX4vdjNUHAABAxjjefVwvtb7k3CNox9EdGrADCeeGI2F9Zuln4sa+dc+3VOQtUo7JSUW5yBCEIgAAAGSMf2z+R61vXD/mnIWlCxWqDOl989434tiU/CnJKg0ZjFAEAACACWHADmjv8b0KRwbPAp3pPaPnHnwubk7QH4z7OsfkqKq8ytkPtNK/ks5wuGyEIgAAAKRF/0C/Xjv8mhpbG/XT3T/VvuZ96jjb4RzPMTk63Xs67uzOsrnLFKoMacXcFQpVhrR87nLO/uCqEYoAAACQMn3RPn1101fVGGnUlgNb1H2+e9S5A3ZAWw5s0XvnvdcZK/IW6aU1L6WiVLgIoQgAAABJcfLcSeWYnLgzOXk5efrO9u/ocNfhhI8p85U5XeGC/qCqZlalqly4GKEIAAAA4+JI1xGnK1xja6N2Ht2pb9/7bX2q+lPOHGOMgpVB/eiNH0mS/FP9ClWGNOPsDH3yrk9qYelCGWPS9RTgUoQiAAAAXDZrrd4++bbCrYMBKBwJ683ON0fMa2xtjAtFkvRo9aO6b8F9CvqDqiyulCQ1NDTourLrUlI7MByhCAAAAJflB7t+oM//8vM6dObQmPNyTI66+rpGjK8KrEpSZcCVIRQBAABghPPR83r18Kt6s/NNfWzJx+KOTS2YmjAQ5XvyVTu71tkPtGzuMjrDISMQigAAAKCe8z3aenCrsx9oy8Et6jnfo9ycXH3w+g/Kl+dz5i6fu1xGRkXeIq3wr1DQH1TQH1TN7BoV5Bak8VkAV4ZQBAAA4EInz51UU6TJCUHb27br/MD5EfP6B/q19eBW3fGuO5yx4oJi7f6j3VpQukC5Ofw6iczH/8UAAAAuY63Vwn9aqGPdx8acVzm1UsHKYMJL4BZNX5Ss8oCUIxQBAABkGWut3jrxltMV7r4F9+l3r/9d57gxRsvnLtfP9v0s7nGLpi+Ku0fQ3KlzU1w5kB6EIgAAgAw3YAe0+9juwfbYkUaFW8NxN0e1snGhSJLuCNyhg6cPKuQPKVgZ1Er/SpX5ylJdOjAhEIoAAAAy0Nsn3tZP9vxEjZFGNUWadOLciVHnNrY2jhj7zNLP6DNLP5PMEoGMQSgCAACY4PqiffJ6vHFjrx95XV/41RdGfcyU/ClaMXeFczmctVbGmGSXCmQkQhEAAMAE03m2U02RJmdP0J7je3T888eVn5vvzFnpXxn3mBmFM+L2Ay0pXyJPjifVpQMZiVAEAACQZm1n2gb3A8VC0K5ju0bM2d62XSv8K5yvpxdO1xeWf0HzS+crVBnS/JL5nAkCrhChCAAAIE0++9+f1c9//XO9deKti87dfWx3XCiSpK/e+dVklQa4CqEIAAAgiQbsgHYd3aWC3AItLFsYd+zNzjcTBiKP8ejWilsV9AcV9A92hiv1laaqZMB1CEUAAADjqC/ap1faXlE4Mng5XNOBJp08d1IP3/Kw/vm+f46bG/KH9MKbL6ggt0C3zbnNCUHL5i5TkbcoTc8AcB9CEQAAwFXo7uvWloNbnHsEbT24VWf7z46Y1xgZ2Rb7o4s/qmBlULfOujWuiQKA1CIUAQAAXKFf/PYXuvc/7lX/QP+Y82YWzdSS8iU6Hz2vPE+eMz536lzNnTo32WUCuAhCEQAAwBgOnT6kcCSspkiT/uG9/xAXahbPWJwwEF0z7Zq49tjzSubRGQ6YwAhFAABkma7eftXvaFNLR7cCpYWqq6pQUT5v+ZfCWqvfdP7GaY0djoTjGiF8vOrjqpld43w9a/IszS+Zr/zcfIX8IQUrB/cEzZ4yOx3lA7hCvEICAJBFtrV0as2GZlkr9fRF5fN6tP75Pdq4tlY1gZJ0lzch7Tq6Sw0tDWqMNCrcGtbR7qOjzm1sbYwLRZK089GdKsgtSHaZAJKIUAQAQJbo6u3Xmg3N6u6NOmM9fYOfr9nQrOZ1q1XIGaMR/vQXf6pfvvXLUY9Pyp3kdIZ7zzXvGXGcQARkPl4ZAQDIEvU72mRt4mPWSvU72/RAjT+1RaVZV1+XthzY4lwOV1NRoyfueiJuTtAfjAtFxQXFWulf6ewJumXWLfJ6vKkuHUAKEYoAAMgSLR3dzpmh4Xr6ompp70lxRanX0dOhTZFNTgh69fCritp3/pucOHdCTyg+FN157Z3adWyXQpUhhSpDunHGjcoxOakuHUAaEYoAAMgSgdJC+byehMHI5/UoUOZLQ1XJ13KyRV/d9FWFI2G9cfyNMefuOrpLJ8+dVHFBsTN225zb9KPf+1GSqwQwkRGKAADIEnVVFVr//J6Ex4yR6pZUpLii8WWtVaQnouhAVJ4cjzNuZPTdV76b8DFGRovLFyvoH+wKF6wMxgUiAJAIRQAAZI2i/FxtXFs7ovucMdLGtbUZ12QhOhDVzqM749pjH+s+piW3LNFNM29y5lUWV8o/1a/IqYhyc3JVXVHt7AdaMXeFpk2alr4nASAjZNarIwAAGFNNoETN61arfmebWtp7FCjzqW5JRUYEot7+Xm1v2+6EoKYDTTrde3rEvHBrOC4USdI/3PUPKi4o1m1zblOhtzBFFQPIFhP/FRIAAFyWwvzcjOsy99n//qy+u/276o32jjmvKLdIPedHNoz40KIPJas0AC5AKAIAAClxvPu4NkU2Kcfk6Heu+524Y5O9kxMGoorJFQpVhpw9Qcf3HNe7V747VSUDcAlCEQAASIrIqYjCrWHncri97XslSdUV1SNCUbAyKIWl+SXznYYIocqQ3lX8LhljnHkNextS+RQAuAShCAAAXDVrrfZ37H+nKUJrWK2nWhPOfe3wazrTe0aT8yc7Y6HKkNoea9OsybNSVTIAOAhFAADgqv32xG91/beuH3NOXk6eqiuqFaoMqTfaq8l6JxQV5BYQiACkDaEIAABc1Ln+c9p2aJvTGvvr7/26riu7zjl+7bRrNbNopo50HXHGfHk+LZ+73NkPtHTOUvnysvMGsgAyG6EIAACMcLr3tDYf2Kxw62AIaj7UHNcI4QMLPxAXiowx+p2Fv6PDXYcV8ocUrAzq5pk3K8+Tl47yAeCyEIoAAIAk6aWWl/SzfT9TY6RRrx95XQN2YNS54UhYj1Q/Ejf23brvJrtEAEgKQhEAAC7U1delIm9R3NgLb76gJ7c+Oepj5pfMd9pj3x64PckV4mK6evtVv6NNLR3dCpQWqq6qQkUZcJNeYCLiJwcAgCxnrdW+9n3vdIaLhDVnyhw1/WFT3LxgZVBf2/w1SZKRUdXMKgX9g62xV/pXambRzHSUjwS2tXRqzYZmWSv19EXl83q0/vk92ri2VjWBknSXB2QcQhEAAFmmf6BfO47siAtB7T3tcXMOnzmss+fPalLeJGdspX+l/nzFnytYGdTyuctVXFCc4spxKbp6+7VmQ7O6e6POWE/f4OdrNjSred1qFXLGCLgs/MQAAJAlTpw9oQefeVBNB5rU1dc15lyvx6v9Hft108ybnLHigmJ9efWXk1wlrlb9jjZZm/iYtVL9zjY9UONPbVFAhiMUAQCQYU6dO6XNBzbrllm3qLyo3BkvLijW9rbtCQNRyaQSpzV2qDKkm2beRGe4DNXS0e2cGRqupy+qlvaeFFcEZD5CEQAAE9yx7mNOa+zG1kbtOLpDA3ZA//r+f9Xam9c684wxWulfqWf3P6s5U+Y4TRFClSFdV3adckxOGp8FxkugtFA+rydhMPJ5PQqUcS8o4HIRigAAmECstWo91apwa9jZE7S/Y3/CuY2RxrhQJElffs+X9eTdT6pyaqWMMakoGSlWV1Wh9c/vSXjMGKluSUWKKwIyH6EIAIAJ5PGGx7W+cf2Yc4yMbpp5kxaULBhx7Prp1yerNEwQRfm52ri2dkT3OWOkjWtrabIAXAF+agAASKH+gX69fuR1NbY2qvNsp/7m3X8Td/zmmTePeIzX41VNRY1zKdzyucs1tWBqqkrGBFQTKFHzutWq39mmlvYeBcp8qltSQSACrhA/OQAAJNHZ82fVfKjZ2Q+05eAWpxFCQW6BvhT6kvJz8535K/0rVeQt0vK5y53GCLWza+NaZwOSVJifS5c5YJwQigAAGEf9A/36xW9/4TRG2Na2TX3RvoRzz/Wf0/a27VrhX+GMTS+crpN/dlKeHE+qSgYA1yMUAQBwFay1cQ0NjIwefOZBne49Pepj5k6Z63SGm1cyb8RxAhEApBahCACAS2StVcvJFqcrXDgS1uO3P66PLv6oM8eT49FK/0q98OYLzth1Zdcp5A8pWDl4OVxlcWU6ygcAjIJQBADAKAbsgPYc3zPYHjvSqHBrWIfOHIqb09jaGBeKJOkjN3xE80vmK1QZ0kr/Ss0onJHKsgEAlykpocgYM13SZyUNWGu/ZIx5SNIXJR2T1GetvSs2b72kUKyOh621bxhjFkr6tqQCSZuttZ9PRo0AAIzmxbde1Debv6lNkU3qPNs55twtB7eMGHuo6iE9VPVQssoDAIyzZJ0p+ntJv5F04ZbKxZK+aK199sIEY0xQUrm19nZjzI2SnpB0j6QnJX3CWttijPmxMWaptXZrkuoEALjY2fNn9euOX6tqZlXc+PGe43pu/3MJH1PkLdKKuSsGO8NVDnaGAwBktqSEImvtx40xqyTdHRsqlrRj2LS7JP0gNn+3MabEGJMrqcBa2xKb84ykZZIIRQCAq3by3Ek1RZqcPUHb27YrPzdfJ/7shHJz3nlLDPqDzudlvjLn/kBBf1BVM6vi5gIAMl+qXtVzJX3NGHNe0vettU9JmiHp+JA5/ZLKJXUMGeuQxK25AQBX5PCZw4MNEWJ7gnYd3SUrGzfnfN95vX7kdVVXVDtjs6fM1vd/9/uqrqjWwtKFcd3lAADZJyWhyFr7uKTHjTE+Sc8aY5oknZI0bci0AUmdGjyrdME0xQcnhzHmYUkPS1J5ebkaGhrGv/Ar1NXVNaHqwfhgXbMT65qdrLX6xLZP6O2X3r7o3EpfpV7a+pK6pnXFjc/RHB3pPKIjOpKsMnEF+JnNXqxtdsqUdU1JKDLG5Fpr+yWdlXRGkpUUlnS/pLAxZpGkg9bas8aYfGPMbGvtIUkflPTXib5n7GzTU5JUXV1tV61alYJncmkaGho0kerB+GBdsxPrmrkG7IDeOPaGwpGwbp55s5bNXRZ3fNrOaXr7bHwoyjE5umXWLYP7gfxBrfSv1PTC6aksG1eJn9nsxdpmp0xZ11RdPvdlY0xt7N/7qbV2jzFmn6R7jDFhDQalR2JzH5P0E2NMr6TnrLV7U1QjAGACOx89r1cPv+rsB9oU2aQT505Ikj5d8+kRoWjJ1CV648wbWjpnqbMnaNmcZZqcPzkd5QMAJrCkhSJrbYOkhtjnI9pqW2sHJD2aYHybBpsrAABcrOd8j7Ye3OqEoC0Ht6jnfE/CueFIeMTY/XPu13c/9l3l5+Ynu1QAQIajfQ4AYEJ6Zs8z+vjPPj7mnOm+6QpVhrQqsErW2riGCIW5hQQiAMAlIRQBANKi7Uybwq1hhSNhvX7kdb205iV5cjzO8WBlcMRjAsWBuPbYC0oX0BkOAHDVCEUAgKSz1uq3J37rhKDG1kb99sRv4+bsPrY77iaqlVMrtfqa1Zo3bZ6ClYONEeZOnZvq0gEALkAoAgAkzb+8+i/65Vu/VLg1rMNdh8ecG46E40KRMUa/fOiXyS4RAABCEQDg6vVF+9RzvkfFBcVx49/f+X01tjYmfExBboGWzl7qXAo3vHscAACpQigCAFy27r5uvXzwZedSuJcPvqxHqx/V37/37+PmBf1BJxRNyZ+iFXNXOCGouqKaRggAgAmBUAQAuKjOs51qijQ57bFfOfyK+gf64+Y0RkaeEbp/0f2aUThDocqQFs9YHNdIAQCAiYJQBAAY1ZYDW/RI/SPadWzXReeeOndK56PnlefJc8ZumnmTbpp5UxIrBADg6hGKAMDlrLX6TedvtPnAZn286uNxLa7LfGWjBqIbpt/gXAoXrAxqzpQ5qSoZAIBxRSgCAJeJDkS169gupz12OBLWka4jkqTa2bW6fvr1ztx5JfNUXliu9p523Vpxq3OPoBVzV6jUV5qupwAAwLgiFAFAluuL9ml723aFW8NqjDSqKdKkU72nEs4NR8JxoehCW+x3TXuXirxFqSoZAICUIhQBQJa78/t3jtoW+4Kp+VO10r9SFZMrRhxbXL44WaUBADAhEIoAIMN19HRoU2STwpGw5pfM1yPVj8QdXzp76YhQNLNoprMfKFQZ0o0zblSOyUll2QAATBiEIgDIMAdPHxy8FC7WHvuN4284x1bMXTEiFAX9QT2z95m4EHTttGvjGioAAOBmhCIAmOA6ejr0030/HWyK0BrW2yffHnVu86FmnT1/VpPyJjljdQvqdN/C+1JRKgAAGYlQBAATSHQgqhyTE3cW53DXYX3y558c9TG5Obm6ddY7neGG3yCVM0IAAIyNUAQAadTb36vtbdudS+GaDjTp1Ydf1bUl1zpzFk1fpJJJJeo82ylJmpQ7SbfNuc25HO62Obep0FuYrqcAAEDGIxQBQAp19XVpy4EtTgjaemirzvWfi5sTjoTjQlGOydFjtz2mPE+eQpUh3TLrFnk93lSXDgBA1iIUAUAKfHPrN/V/dv4fvXr4VUVtdMy5rx1+TWtuWhM39hehv0hidQAAuBuhCADG0YFTB3Ty3MkR9/Z568Rb2ta2LeFj5pXMc/YDBf1BXTPtmlSUCgAAYghFAHCFrLXa37Ff4dawwpHBFtmtp1q1KrBK//cP/m/c3FBlSN/Y+g0ZGS0uX6yQP6RgZVBBf1CzJs9K0zMAAAASoQgALll0IKodR3c4+4HCrWEd7zk+Yt7LB19WX7Qvbt/PHYE7VP9gvZbPXa5pk6alsmwAAHARhCIAuARvnXhLN//zzTrde3rMeb48n5bNWab2nnZVTK5wxqdNmqZ7F9yb7DIBAMAVIBQBGFVXb7/qd7SppaNbgdJC1VVVqCg/e182zvSe0eYDmxWOhPVHNX8UF2oqp1YmfMy0gmla6V/p7Ae6ZdYtyvPkpapkAAAwDrL3txsAV2VbS6fWbGiWtVJPX1Q+r0frn9+jjWtrVRMoSXd54+J493E1Hm/Us//9rMKRsF478poG7IAk6fqy6/X7S37fmevJ8Wj53OXaeXSnE4CC/qBumHGDckxOup4CAAAYB4QiACN09fZrzYZmdfe+0zq6p2/w8zUbmtW8brUKM/CM0cHTB/VSy0tqbG1UY6RR+9r3jTo3HAnHhSJJ+tH9P1KRt0jGmGSXCgAAUijzfqsBkHT1O9pkbeJj1kr1O9v0QI0/tUWNgy+Hv6xvb//2qMeNjJaUL1GoMqT7Ftw34vjk/MnJLA8AAKQJoQjACC0d3c6ZoeF6+qJqae9JcUUX1z/Qrx1Hdgx2hYuEVZBboH//4L/HzQlWBuNCUV5OnhYULVDd4joF/UGt8K9QcUHxRf8tt+21AgAg2/EuDmCEQGmhfF5PwmDk83oUKPOloap45/rPqflQs3OPoM0HNutM3xnneJG3SP0D/crNeedlLugPavU1q50bpdbOrlVzU7NWrVp1yf+uG/ZaAQDgNoQiACPUVVVo/fN7Eh4zRqpbUpHwWLKd7j2tr2z6isKRsJoPNasv2jfq3K6+Lr1+5HVVV1Q7Y7OnzNYvH/rlFf/72brXCgAAt6NlEoARivJztXFtrQrzPfJ5PZIGzxAV5nti48n/xf9Y9zF193XHjRXkFugbW7+hTZFNCQPR7Mmz9eCND+o7935Hux/drVtm3TKuNV3KXisAAJB5+JMmgIRqAiVqXrda9Tvb1NLeo0CZT3VLKpIWiFpPtqqxtdHZE7SvfZ9+dP+P9Hs3/J4zx+vxatmcZXrx7RclSQtKFziXwgX9QQWKA0ntDJeJe60AAMDFEYoAjKowPzcpXeastdrbvvedENQa1oHTB0bMC0fCcaFIkj63/HP6VPWnFPQHVV5UPu61jSUT9lrh0tEwAwBwAa/+AFLqW83f0uMNj6vjbMeY8/Jy8tTV1zVi/O55dyertIuaqHutcPlomAEAGIpQBGDcnT1/Vs2HmnW467A+cuNH4o5Nzp+cMBAV5hVq+dzlcZ3hJuVNSlXJl+TCXqvhv0wbo5TttcLVo2EGAGA4XvUBXLVT506p6UCT0x57W9s29UX7NK1gmj58w4eVY97p6RL0ByVJpZNKFawMKugf/Lh51s1x7bMnqlTvtcL4y9abEwMArhzv4gAu29Guo85eoMZIo3Yc2SGrkb9lnjh3Qm8ce0OLyxc7Y4HigPb+j71aULogLixlkmTttUJq0DADADAcoQjAZemL9qnyyUr1RnvHnLewdKFClSF5Pd64cWOMriu7LpklAmOiYQYAYDhCEYA4A3ZAe4+/0xnuD2/+Q62+ZrVz3OvxqnZ2rcKRsDOWY3J008ybnP1AK/0rNaNwRjrKBxwDVnq6OTKiuxwNMwAAwxGKAJfrH+jXa4dfi7tHUOfZTud4xeSKuFAkSXdec6esrBOCls9drin5U1JdOjCqbS2d2nv4tL61b0/C7nI0zAAADMUrP+BCe47v0TN7nlE4EtbmA5vVfb571LlDzwhd8KXbv6Qv3f6lZJYIXLEL3eU+tcA6l8gN7y5HwwwAwFC8+gNZ7lz/ORXkFsSNbT6wWX/Z8JejPqbMV+Z0hbs9cHuySwTG1aV2l6NhBgDgAkIRkGWOdB1xWmM3tjbqaPdRtT3WJmOMM+dCW+wLKqdWxrXHvq7surj5GD9dvf2q39E2Yp8Lxg/d5QAAl4t3YiCDWWv19sm3B/cDxYLQm51vjpi3v2N/XMe3BaUL9Nmln1V1RbWClUH5p/LX8lTY1tI5Yh/L0H0uGB8XustJ/SOO0V0OAJAIoQjIQNZa/cHP/kAvvv2i2s60jTk3x+Ro97HdcaHIGKOv3/31ZJeJIS7sc+nufecMxvB9LuxnGR90lwMAXC7egYEJ7Hz0vF478prKfGW6Zto1zrgxRr/u+HXCQJTvydfSOUudS+GWzV1GZ7gJ4FL3ueDqFeXnauPaWjVv3uTcj4jucgCAsfDOAEwgPed7tPXgVqc99paDW9RzvkdfXPlF/d17/i5ubtAf1NZDWzXZO1nL5y5XqDKkUGVI1RXVIxorIP3Y55JaNYESnXl7ih6ffw3d5QAAF8W7A5BGJ86eUNOBJmc/0Pa27To/cH7EvMbWxhFjn6r+lB5c/KCWlC9Rbg4/yhPdhX0uiYIR+1ySI8eIs28AgEvCb1JAmvxg1w/0+//5+7Ia5ZqqmEBxQNeXXS9rbVxHuGtLrk12iRhH7HMBAGDiIhQBSWKt1Vsn3lI4EtbrR17X19/79bhQs7h8ccJAtGj6IgX9QYUqQwr6g5o7dW4qy0aSXNjnMrz7HPtcAABIP96FgXEyYAe0+9hu51K4cCQc1wjhM0s/E9csYdH0RZpROEP+qX6F/CEFK4Na6V+pMl9ZOspHCtQEStS8brXqd7axzwUAgAmEd2LgKmw9uFUvtb6kcCSspkiTTpw7MerccGs4LhTlmBwd+JMD8nq8qSgVE0Rhfi77XAAAmGAIRcBVePT5R/XakddGPT4lf4pWzF2hoD+o2+bcNuI4gQgAACD9CEXAKE6cPaFNkU0KR8JqbG3UjXk3apVWxc0J+oNxoWhG4Qzn/kChypCWlC+RJ8eT4soBAABwOQhFQEzbmTZnP1Bja6N2H9sd1wihr7hvxGPuXXCvTvaedELQ/JL5cc0UAAAAMPERiuBqbxx7Q/9zy/9UuDWs35747Zhz957eq/PR88rz5Dljd117l+669q5klwkAAIAkIhTBFQbsgPYe36sbZtwQN36u/5w2vr4x4WM8xqNbZt3itMbWAcUFIgAAAGQHQhGyUl+0T6+0veJcCtd0oEknz53UgT85oDlT5jjzqmZWabJ3ss70nVFBboFum3Ob0x77tjm3qchb5MxtONKQhmcCAACAZCMUISt093Xr5YMvq7G1UeFIWC8ffFln+8+OmBduDevBxQ86X+fm5Op/3fe/5J/q160Vt9INDgAAwIUIRch4H/vPj+mHb/xQ/QP9Y84rLyxXV1/XiPEHbnwgWaUBAAAgAxCKkBEOnT6kcCSs4oJi3T3v7rhjk72TEwaia6Zd4+wHCvqDmlcyj85wAAAAGIFQhAnHWqvfdP7GuRSusbVRb598W5L03mvfOyIUhSpD+u4r39WNM2509gMF/UHNnjI7HeUDAAAgwxCKkHbRgah2HdulcGtYjZFGhVvDOtp9NOHczQc2KzoQjbsh6vsXvl/tn29Xqa80VSUDAAAgixCKkHbb2rZp2feWjTnnQme42ytv19n+s3Fd4Qq9hSr0Fia7TAAAAGQpQhGSrquvS1sObFE4ElY4EtbTH3pa5UXlzvFbZt2iSbmT4rrFFRcUa8XcFc6eIDrDAQAAIFkIRRh3HT0d2hTZ5OwHevXwq4raqHM8HAnr/kX3O197PV594LoPKGqjCvqDClWGdOOMG5VjctJRPgAAAFyGUIRx8cKbL+jn+3+ucCSsN46/MebccGt8KJKk//jQfySzPAAAAGBUhCJcFmutzvSd0ZT8KXHj/7n3P/W9176X8DFGZrAzXOxSuFBlKBWlAgAAAJeEUIQxRQei2nl0p9MeOxwJa+nspXruwefi5gX9QScU5ebkqrqi2rk/0Ar/CpVMKklH+QAAAMBFEYoQp7e/V9vatjntsTcf2KzTvafj5myKbNKAHYjb8/Oea96jv7r9rxSsDGrp7KV0gwMAAEDGIBRBkhQ5FdFDP31IWw9uVW+0d8y5VlYHTh1QZXGlMzZnyhw9vurxZJcJAAAAjDtCkcu097RrU2ST7gjcoakFU53xGYUz9PLBl9UX7RvxmIrJFc6lcKHKkG6YcQOd4QAAAJA1CEVZ7sCpA85+oMbWRu1t3ytJevYjz+r9C9/vzCvILVDt7FptimzSvJJ5CvlDClYOBqFrpl0jY0y6ngIAAACQVISiLGKt1f6O/Qq3hp0Q1HqqNeHccGs4LhRJ0nfu/Y5KJ5Vq1uRZqSgXAAAAmBAIRVnk0ecf1T+/8s9jzsnLyVN1RbWumXbNiGM3zrgxWaUBAAAAExahKIOc6z+nbYe2KRwJS5LWBdfFHb911q0jHuPL82nZnGXOPYKWzlkqX54vJfUCAAAAmYBQNIGd6T2jzQc2O5fCNR9qdjrDzSicoS+u/GLcXp9gZVAlk0q00r/S2RN088yblefJS9dTAAAAACY8QtEEcq7/nF548wVnT9BrR17TgB1IOPdY9zH9uuPXWli20BlbWLpQxz9/nM5wAAAAwGUgFKWRtTbuTE//QL8+/OMPK2qjoz5mfsl851K4GYUz4o4ZY2RElzgAAAC36urtV/2ONrV0dCtQWqi6qgoV5fMr/8XwXyhFrLXa174vrj32U/c9pbvn3e3MKfIW6daKW9V8qFmSZGRUNbPKuT/QSv9KzSyama6nAAAAgAlsW0un1mxolrVST19UPq9H65/fo41ra1UTKEl3eRMaoShJ+gf69fqR151L4cKRsNp72uPmhFvDcaFIktZUrdG7A+9WsDKo5XOXq7igOIVVAwAAIBN19fZrzYZmdfe+c8VRT9/g52s2NKt53WoVcsZoVPyXGWc/2/cz/e3Ov9W+LfvU1dc15tzmtuYRY4/WPJqs0gAAAJCl6ne0ydrEx6yV6ne26YEaf2qLyiCEonF26PQhbT+xPeGxoZ3hQpUh3Tzr5hRXBwAAgGzU0tHtnBkarqcvqpb2nhRXlFkIReMsVBlyPp8zZY6zHyjoD+r66dfTGQ4AAADjLlBaKJ/XkzAY+bweBcq4T+VYCEXj7IYZN2jddev0yfd+UpVTK+O6ywEAAADJUFdVofXP70l4zBipbklFiivKLJy2GGc5Jkd3lt+pQHGAQAQAAICUKMrP1ca1tSrM98jn9UgaPENUmO+JjXMuZCz81wEAAACyQE2gRM3rVqt+Z5ta2nsUKPOpbkkFgegS8F8IAAAAyBKF+bl0mbsCXD4HAAAAwNUIRQAAAABcjcvnXKart1/1O9rU0tGtQGmh6qoqVMR1pgAAAHAxfht2kW0tnVqzoVnWDt7Ey+f1aP3ze7Rxba1qAiXpLg8AAABICy6fc4mu3n6t2dCs7t6oc1Ovnr6ounujsfH+NFcIAJAGX6+fbo7oK/+1V083R9TF6zMAJB1nilyifkebrE18zFqpfmcbnUoAIM04ow8A6cGZIpdo6eh2zhAN19MXVUt7T4orAgAMxRl9AEifpIQiY8x0Y8zfGmPWx75eaIx50RjTZIx5Ysi89caYl2LjN4w1F1cnUFro3N14OJ/Xo0CZL8UVAQCGupQz+gCA5EjWmaK/l9QrKS/29ZOSPmGtXSEpYIxZaowJSiq31t4u6RFJT4w2N0k1ukpdVYWMSXzMGKluSUVqCwIAxOGMPgCkT1JCkbX245IaJckYkyupwFrbEjv8jKRlku6S9IPY/N2SSsaYi6tUlJ+rjWtrVZjvcc4Y+bweFeZ7YuNsLwOAdOKMPgCkj7Gjnau/2m9szCpJd0v6hqR/tNbeHxu/U9JKSTNj47tj45skPSDpG8PnWmsfT/D9H5b0sCSVl5ff+vTTTyfleVyJrq4uFRUVpbuMhAasdOpsn3r7B5Sfm6Opk7zKGeUMEuJN5HXFlWNdJ5bxfI3KtLUdsNLew6c1kOB9OccYXT9rCq/Xyrx1xaVjbbPTRFrXO+644xVrbXWiY6k4PXBSUvGQr6dJOi5pUuzzCwYkdY4ydwRr7VOSnpKk6upqu2rVqnEq9+o1NDRoItWD8cG6ZifWdeIY2XlNMubcFXdey8S1nZyg+5wxovvcEJm4rrg0rG12ypR1TXoostaeNcbkG2NmW2sPSfqgpL+WNE/S/ZLCxphFkg6OMRcAkMWGdl674ML+mjUbmtW8brUrLvOtCZSoed1q1e9sU0t7jwJlPtUtqXDFcweAdErVq+xjkn5ijOmV9Jy1dq8xZr+ke4wxYUlnNNhsIeHcFNUIAEgT7qX2jsL8XNc8VwCYKJIWiqy1DZIaYp9v07CGCdbaAUmPJnjciLkAgOxG5zUAQDpx81YAQNrReQ0AkE6EIgBA2nEvNQBAOhGKAABpx73UAADpxLsMAGBCoPMaACBdeKcBAEwYdF4DAKQDl88BAAAAcDVCEQAAAABXIxQBAAAAcDX2FAEAENPV26/6HW1q6ehWoLRQdVUVKqLRAwBkPV7pAQCQtK2lU2s2NMtaqacvKp/Xo/XP79HGtbWqCZSkuzzA1fiDBZKN/5sAAK7X1duvNRua1d0bdcZ6+gY/X7OhWc3rVtMaHEgT/mCBVGBPEQDA9ep3tMnaxMeslep3tqW2IACS4v9gceEPFT19UXX3RmPj/WmuENmCUAQAcL2Wjm7nF67hevqiamnvSXFFACT+YIHUIRQBAFwvUFoon9eT8JjP61GgzJfiigBI/MECqUMoAgC4Xl1VhYxJfMwYqW5JRWoLAiCJP1ggdQhFAADXK8rP1ca1tSrM9zi/gPm8HhXme2LjNFkA0oE/WCBVeJUHAIybTG6bWxMoUfO61arf2aaW9h4FynyqW1JBIALS6MIfLIZ3nzNG/MEC44r/kwAA4yIb2uYW5ufqgRp/ussAMAR/sEAq8H8TAOCqcZ8fAMnEHyyQbOwpAgBcNdrmAgAyGaEIAHDVaJsLAMhkhCIAwFWjbS4AIJMRigAAV422uQCATEYoAgBcNe7zAwDIZLxLAQDGBW1zAQCZincqAMC4oW0uACATEYoAII26evtVv6NNLR3dCpQWqq6qQkWcWQEAIKV45wWANNnW0qk1G5pl7WDbap/Xo/XP79HGtbWqCZRc8fclaAEAcHl4lwSANOjq7deaDc3q7n3n3j4X7vOzZkOzmtetvqK9OMkKWgAAZDO6zwFAGtTvaJO1iY9ZK9XvbLvs7zk0aF0IWD19UXX3RmPj/VdTMgAAWYtQBABp0NLR7QSX4Xr6ompp77ns75mMoAUAgBsQigAgDQKlhc79fIbzeT0KlPku+3smI2gBAOAGhCIASIO6qgoZk/iYMVLdkorL/p7JCFoAALgBoQgA0qAoP1cb19aqMN/jBBmf16PCfE9s/PKbLCQjaAEA4AZ0nwOANKkJlKh53WrV72xTS3uPAmU+1S2puKJAJL0TtIZ3nzNGVxy0AABwA94hASCNCvNz9UCNf9y+33gHLQAA3IB3SQDIMuMdtAAAyHbsKQIAAADgaoQiAAAAAK5GKAIAAADgaoQiAAAAAK5GKAIAAADgaoQiAAAAAK5GKAIAAADgaoQiAAAAAK5GKAIAAADgaoQiAAAAAK5GKAIAAADgaoQiAAAAAK5GKAIAAADgaoQiAAAAAK5GKAIAAADgaoQiAAAAAK5GKAIAAADgaoQiAAAAAK5GKAIAAADgasZam+4arpox5rik1nTXMUSZpPZ0F4Fxx7pmJ9Y1e7G22Yl1zV6sbXaaSOtaaa2dnuhAVoSiicYYs91aW53uOjC+WNfsxLpmL9Y2O7Gu2Yu1zU6Zsq5cPgcAAADA1QhFAAAAAFyNUJQcT6W7ACQF65qdWNfsxdpmJ9Y1e7G22Skj1pU9RQAAAABcjTNFAAAAAFyNUJSAMWa6MeZvjTHrY18vNMa8aIxpMsY8MWTeemPMS7HxG8ZrLpLDGFNsjHnaGNNgjGk0xryLtc0OxhivMebnsbV9yRgzm7XNHsaYV40xd7Om2cMYsyv289pgjPkoa5s9jDG1sffYJmPMF1jbzGeM+fSQn9cGY0x7Vq6rtZaPYR+S/rekv5T0ldjX/yUpEPv8x5KWSgpKeio2dqOkF8ZjbrqfezZ/SKqQVBH7/F5J32Jts+NDg3/g8cU+/5ikdaxtdnxIul/SbyXdzZpmz4ekXw37mrXNgg9JeZLqJU1jbbPzQ9KHJH0uG9c1VxjBWvtxY8wqSXcbY3IlFVhrW2KHn5G0TFKppB/E5u82xpSM09ytyX127mWtbRvy5QlJvWJts4K1dkBST+zL+ZK2S7qTtc1sxpjJkh6S9O+SeC3OLgMXPuF9Nqu8T1KrpB8YY/IkfVGsbdYwxuRI+h+S3i/p3mxbVy6fu7jpkjqGfN0haZqkGZKODxnvl1Q+DnORZMaY2Rr8K8ffi7XNGsaYzxtj3pRULelVsbbZ4JuS/kaDv0BPFmuaFYwxhZKujV1i9SNJs8TaZov5kkok1Un6hKQfirXNJr8j6ZfK0tdjzhRd3ElJxUO+nqbBRZyk+IUakNQ5DnORRMaYOkn3SfqkBs8sFA85zNpmMGvtE5KeMMa8T9I/iLXNaMaY35cUsdZuM8bcK16Ls4a1tlvStZJkjLlT/Lxmk35Jv7DW9ktqMcZ0Kn5dWNvM9ocaDLtnlIU/s5wpughr7VlJ+bGzC5L0QUkvSgpr8Fp3GWMWSTo4TnORJMaYJZLus9Y+Yq3tYG2zhzFmsjHGxL6MSPKItc10H5W0yBjztAbX4c8k3cCaZj5jjGfIl8clWfHzmi22aPASOhljyjX4y7OXtc18xphSDV7adixbf3/iTNGleUzST4wxvZKes9buNcbsl3SPMSaswR/6R8ZjbiqflAvdLSlojGmIfR0Ra5strpP0ZOy/91lJn5ZUJtY2Y1lr773wuTHmryS9rMFLKVjTzDfPGPOvkvpiH49qcH8Ba5vhrLXNxpj9xpgmDZ41ekyDf4BnbTNfSIOh94Ks+/2Jm7cCAAAAcDUunwMAAADgaoQiAAAAAK5GKAIAAADgaoQiAEBGMsbUGGMeS3cdAIDMR/c5AMCEFmvh/KSk6yXlSfoXa+33JeVLmjJk3s8kFQ17eJWkCmvt+QTf92FJudbabyencgBApiAUAQAmuj+U9Ja19o9jAenHxphNwydZaz8wfMwY87wGWwMPH58n6d7BT80vrLW/Gf+yAQCZglAEAJjoqiR9U5KstVFjzK8k3SDp5KU82A6594Qx5kEN3m/jpKSPafAy8r80xkyT1GSt/d64Vg4AyAiEIgDARPeKpLsk/doYYzQYar4gyX8Jj40O+7pZ0k+tteeGjP2pMcYnac54FAsAyDzcvBUAMKEZY3IkfUXStRrcU/S/rbU/McaslLRaUpOkvxjykDmSeiR1Dhn7iqTzkr54kX/ua9baX4xX7QCAzEAoAgBMeMaYUklnrbU9Q8ZWSlptrf2rYXM/K2mftfa/L/I9P6bBRgsbx71gAEBG4fI5AEAmeFTSJkkNFwastZtiYwAAXBXuUwQAAADA1ThTBADIFE8aY04OG3vdWvvZK/x+RyV5rqoiAEBWYE8RACCrGGOKJJ231vamuxYAQGYgFAEAAABwNfYUAQAAAHA1QhEAAAAAVyMUAQAAAHA1QhEAAAAAVyMUAQAAAHA1QhEAAAAAVyMUAQAAAHC1/x8h3AmWhCx7kQAAAABJRU5ErkJggg==",
      "text/plain": [
       "<Figure size 1008x720 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "def drawGraph():\n",
    "    \n",
    "    plt.figure(figsize=(14,10))\n",
    "    plt.scatter(data_result['인구수'], data_result['소계'], s=50)\n",
    "    plt.plot(fx, f1(fx), ls='dashed', lw=3, color='g')\n",
    "    plt.xlabel('인구수')\n",
    "    plt.ylabel(\"CCTV\")\n",
    "    plt.grid(True)\n",
    "    plt.show()\n",
    "\n",
    "drawGraph()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 7. 강조하고 싶은 데이터를 시각화해보자"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 그래프 다듬기\n",
    "#### 경향과의 오차 만들기\n",
    "- 경향(trend)과의 오차를 만들자\n",
    "- 경향은 f1 함수에 해당 인구를 입력\n",
    "- f1(data_result['인구수'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 241,
   "metadata": {},
   "outputs": [],
   "source": [
    "fp1 = np.polyfit(data_result['인구수'], data_result['소계'],1)\n",
    "f1 = np.poly1d(fp1)\n",
    "fx = np.linspace(100000, 700000, 100)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 242,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>소계</th>\n",
       "      <th>최근증가율</th>\n",
       "      <th>인구수</th>\n",
       "      <th>한국인</th>\n",
       "      <th>외국인</th>\n",
       "      <th>고령자</th>\n",
       "      <th>외국인비율</th>\n",
       "      <th>고령자비율</th>\n",
       "      <th>CCTV비율</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>구별</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>강남구</th>\n",
       "      <td>3238</td>\n",
       "      <td>150.619195</td>\n",
       "      <td>561052</td>\n",
       "      <td>556164</td>\n",
       "      <td>4888</td>\n",
       "      <td>65060</td>\n",
       "      <td>0.871220</td>\n",
       "      <td>11.596073</td>\n",
       "      <td>0.577130</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>강동구</th>\n",
       "      <td>1010</td>\n",
       "      <td>166.490765</td>\n",
       "      <td>440359</td>\n",
       "      <td>436223</td>\n",
       "      <td>4136</td>\n",
       "      <td>56161</td>\n",
       "      <td>0.939234</td>\n",
       "      <td>12.753458</td>\n",
       "      <td>0.229358</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>강북구</th>\n",
       "      <td>831</td>\n",
       "      <td>125.203252</td>\n",
       "      <td>328002</td>\n",
       "      <td>324479</td>\n",
       "      <td>3523</td>\n",
       "      <td>56530</td>\n",
       "      <td>1.074079</td>\n",
       "      <td>17.234651</td>\n",
       "      <td>0.253352</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "       소계       최근증가율     인구수     한국인   외국인    고령자     외국인비율      고령자비율  \\\n",
       "구별                                                                        \n",
       "강남구  3238  150.619195  561052  556164  4888  65060  0.871220  11.596073   \n",
       "강동구  1010  166.490765  440359  436223  4136  56161  0.939234  12.753458   \n",
       "강북구   831  125.203252  328002  324479  3523  56530  1.074079  17.234651   \n",
       "\n",
       "       CCTV비율  \n",
       "구별             \n",
       "강남구  0.577130  \n",
       "강동구  0.229358  \n",
       "강북구  0.253352  "
      ]
     },
     "execution_count": 242,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data_result.head(3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 243,
   "metadata": {},
   "outputs": [],
   "source": [
    "data_result['오차'] = data_result['소계'] - f1(data_result['인구수'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 244,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>소계</th>\n",
       "      <th>최근증가율</th>\n",
       "      <th>인구수</th>\n",
       "      <th>한국인</th>\n",
       "      <th>외국인</th>\n",
       "      <th>고령자</th>\n",
       "      <th>외국인비율</th>\n",
       "      <th>고령자비율</th>\n",
       "      <th>CCTV비율</th>\n",
       "      <th>오차</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>구별</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>강남구</th>\n",
       "      <td>3238</td>\n",
       "      <td>150.619195</td>\n",
       "      <td>561052</td>\n",
       "      <td>556164</td>\n",
       "      <td>4888</td>\n",
       "      <td>65060</td>\n",
       "      <td>0.87122</td>\n",
       "      <td>11.596073</td>\n",
       "      <td>0.57713</td>\n",
       "      <td>1524.595142</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "       소계       최근증가율     인구수     한국인   외국인    고령자    외국인비율      고령자비율  \\\n",
       "구별                                                                       \n",
       "강남구  3238  150.619195  561052  556164  4888  65060  0.87122  11.596073   \n",
       "\n",
       "      CCTV비율           오차  \n",
       "구별                         \n",
       "강남구  0.57713  1524.595142  "
      ]
     },
     "execution_count": 244,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data_result.head(1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 245,
   "metadata": {},
   "outputs": [],
   "source": [
    "# 경향과 비교해서 데이터의 오차가 너무 나는 데이터를 계산\n",
    "\n",
    "df_sort_f = data_result.sort_values(by='오차', ascending=False) #내림차순\n",
    "df_sort_t = data_result.sort_values(by='오차', ascending=True) #오름차순"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 246,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>소계</th>\n",
       "      <th>최근증가율</th>\n",
       "      <th>인구수</th>\n",
       "      <th>한국인</th>\n",
       "      <th>외국인</th>\n",
       "      <th>고령자</th>\n",
       "      <th>외국인비율</th>\n",
       "      <th>고령자비율</th>\n",
       "      <th>CCTV비율</th>\n",
       "      <th>오차</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>구별</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>강남구</th>\n",
       "      <td>3238</td>\n",
       "      <td>150.619195</td>\n",
       "      <td>561052</td>\n",
       "      <td>556164</td>\n",
       "      <td>4888</td>\n",
       "      <td>65060</td>\n",
       "      <td>0.871220</td>\n",
       "      <td>11.596073</td>\n",
       "      <td>0.577130</td>\n",
       "      <td>1524.595142</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>양천구</th>\n",
       "      <td>2482</td>\n",
       "      <td>34.671731</td>\n",
       "      <td>475018</td>\n",
       "      <td>471154</td>\n",
       "      <td>3864</td>\n",
       "      <td>55234</td>\n",
       "      <td>0.813443</td>\n",
       "      <td>11.627770</td>\n",
       "      <td>0.522507</td>\n",
       "      <td>887.835545</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>용산구</th>\n",
       "      <td>2096</td>\n",
       "      <td>53.216374</td>\n",
       "      <td>244444</td>\n",
       "      <td>229161</td>\n",
       "      <td>15283</td>\n",
       "      <td>36882</td>\n",
       "      <td>6.252148</td>\n",
       "      <td>15.088118</td>\n",
       "      <td>0.857456</td>\n",
       "      <td>821.403817</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>서초구</th>\n",
       "      <td>2297</td>\n",
       "      <td>63.371266</td>\n",
       "      <td>445401</td>\n",
       "      <td>441102</td>\n",
       "      <td>4299</td>\n",
       "      <td>53205</td>\n",
       "      <td>0.965198</td>\n",
       "      <td>11.945415</td>\n",
       "      <td>0.515715</td>\n",
       "      <td>743.883771</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>은평구</th>\n",
       "      <td>2108</td>\n",
       "      <td>85.237258</td>\n",
       "      <td>491202</td>\n",
       "      <td>486794</td>\n",
       "      <td>4408</td>\n",
       "      <td>74559</td>\n",
       "      <td>0.897390</td>\n",
       "      <td>15.178888</td>\n",
       "      <td>0.429151</td>\n",
       "      <td>491.405033</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "       소계       최근증가율     인구수     한국인    외국인    고령자     외국인비율      고령자비율  \\\n",
       "구별                                                                         \n",
       "강남구  3238  150.619195  561052  556164   4888  65060  0.871220  11.596073   \n",
       "양천구  2482   34.671731  475018  471154   3864  55234  0.813443  11.627770   \n",
       "용산구  2096   53.216374  244444  229161  15283  36882  6.252148  15.088118   \n",
       "서초구  2297   63.371266  445401  441102   4299  53205  0.965198  11.945415   \n",
       "은평구  2108   85.237258  491202  486794   4408  74559  0.897390  15.178888   \n",
       "\n",
       "       CCTV비율           오차  \n",
       "구별                          \n",
       "강남구  0.577130  1524.595142  \n",
       "양천구  0.522507   887.835545  \n",
       "용산구  0.857456   821.403817  \n",
       "서초구  0.515715   743.883771  \n",
       "은평구  0.429151   491.405033  "
      ]
     },
     "execution_count": 246,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# 경향 대비 CCTV를 많이 가진 구\n",
    "df_sort_f.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 247,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>소계</th>\n",
       "      <th>최근증가율</th>\n",
       "      <th>인구수</th>\n",
       "      <th>한국인</th>\n",
       "      <th>외국인</th>\n",
       "      <th>고령자</th>\n",
       "      <th>외국인비율</th>\n",
       "      <th>고령자비율</th>\n",
       "      <th>CCTV비율</th>\n",
       "      <th>오차</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>구별</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>강서구</th>\n",
       "      <td>911</td>\n",
       "      <td>134.793814</td>\n",
       "      <td>608255</td>\n",
       "      <td>601691</td>\n",
       "      <td>6564</td>\n",
       "      <td>76032</td>\n",
       "      <td>1.079153</td>\n",
       "      <td>12.500021</td>\n",
       "      <td>0.149773</td>\n",
       "      <td>-867.826723</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>송파구</th>\n",
       "      <td>1081</td>\n",
       "      <td>104.347826</td>\n",
       "      <td>671173</td>\n",
       "      <td>664496</td>\n",
       "      <td>6677</td>\n",
       "      <td>76582</td>\n",
       "      <td>0.994825</td>\n",
       "      <td>11.410173</td>\n",
       "      <td>0.161061</td>\n",
       "      <td>-785.029081</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>중랑구</th>\n",
       "      <td>916</td>\n",
       "      <td>79.960707</td>\n",
       "      <td>412780</td>\n",
       "      <td>408226</td>\n",
       "      <td>4554</td>\n",
       "      <td>59262</td>\n",
       "      <td>1.103251</td>\n",
       "      <td>14.356800</td>\n",
       "      <td>0.221910</td>\n",
       "      <td>-591.904555</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>도봉구</th>\n",
       "      <td>825</td>\n",
       "      <td>246.638655</td>\n",
       "      <td>346234</td>\n",
       "      <td>344166</td>\n",
       "      <td>2068</td>\n",
       "      <td>53488</td>\n",
       "      <td>0.597284</td>\n",
       "      <td>15.448512</td>\n",
       "      <td>0.238278</td>\n",
       "      <td>-590.673904</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>광진구</th>\n",
       "      <td>878</td>\n",
       "      <td>53.228621</td>\n",
       "      <td>372298</td>\n",
       "      <td>357703</td>\n",
       "      <td>14595</td>\n",
       "      <td>43953</td>\n",
       "      <td>3.920247</td>\n",
       "      <td>11.805865</td>\n",
       "      <td>0.235833</td>\n",
       "      <td>-573.797784</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "       소계       최근증가율     인구수     한국인    외국인    고령자     외국인비율      고령자비율  \\\n",
       "구별                                                                         \n",
       "강서구   911  134.793814  608255  601691   6564  76032  1.079153  12.500021   \n",
       "송파구  1081  104.347826  671173  664496   6677  76582  0.994825  11.410173   \n",
       "중랑구   916   79.960707  412780  408226   4554  59262  1.103251  14.356800   \n",
       "도봉구   825  246.638655  346234  344166   2068  53488  0.597284  15.448512   \n",
       "광진구   878   53.228621  372298  357703  14595  43953  3.920247  11.805865   \n",
       "\n",
       "       CCTV비율          오차  \n",
       "구별                         \n",
       "강서구  0.149773 -867.826723  \n",
       "송파구  0.161061 -785.029081  \n",
       "중랑구  0.221910 -591.904555  \n",
       "도봉구  0.238278 -590.673904  \n",
       "광진구  0.235833 -573.797784  "
      ]
     },
     "execution_count": 247,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# 경향 대비 CCTV를 적게 가진 구\n",
    "df_sort_t.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 270,
   "metadata": {},
   "outputs": [],
   "source": [
    "from matplotlib.colors import ListedColormap\n",
    "\n",
    "# colormap 을 사용자 정의 (user define)로 세팅\n",
    "\n",
    "color_step = ['#e74c3c', '#2ecc71', '#95a9a6', '#2ecc88', '#3498db', '#3498db']\n",
    "my_cmap = ListedColormap(color_step)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 279,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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Gn2sfXw+nyTJ4/E0eV8ALctG71b50DdCXUZIcE0TANAmhLmM/nxmV0W6jWouWBTpNhrZO1qje9c/1ef888/XsmXL9PTTT6usrEyVlZV69913NWPGDF155ZUBfU888UT17NlTq1atctqstXriiSc0YMAATZs2TZJ0zjnn6Je//KV++ctfKjU19ZA+U0lJiTwej9xufl8HoPXgXyQAQJtxUvdIvfqTXnr123x9tbVE8ZFh+sngWI3pE13nFYJ9kpKS9NFHH+muu+7StGnT5PP5NHjwYL3xxhsaN25cQN/PP/9cSUlJ+vzzz522O+64Q16vV4sWLdKIESOUlJSk22+/3dl+qNOOCgoKFBcXd0j7AkBLISAAANqUnh3DddvIzk3eb+DAgfrvf//bYD+Px+OsLrRz507dfvvtWrJkiTIzM5WYmKh58+YpLS1NmZmZeuyxx3T00bUe1SNJBw0s9fXduHGjevbs2ej9AKAlMMUIAIBql1xyiSIjI533Tz31lPbs2aMFCxYoMTFRktSrVy8tXrxYo0aNUpcuXeo9lrW21mvdunXyeDx1brPWEg4AtAoEBABAu+H3+/XMM89o1KhR6tSpkxISEhQbG6vU1FRdd911+vOf/6zY2Fin//3336833nhDpaWluvPOO532qKgo3XXXXU5oAIAjCQEBANBuTJkyRU8++aTuu+8+bdmyRXl5edqzZ4/mzp0rr9erk08+uc6Hlu3atUt/+9vf6j3uVVddpUmTJrVk6QAQNAQEAEC78e6772rKlCk688wzFRER4bT37dtXjz32mEpLS7VkyZImH3fo0KEaMmRIc5YKACFDQAAAtBtpaWl69NFH9cknn6iiosJpX7dunW6++WbnKgIAtGesYgQAaDceeughJScn65577tEPP/wga60qKirUtWtXnXHGGVqyZIkSEhLq3HfPnj3yer31Hrt3797KyspqqdIBIGgICACAdsPlcmny5MmaPHlyk/YbMmRIk566XJ/Y2FhNmTLlsI8DAC2JKUYAAARJfHy88yRmAGitCAgAAAAAHAQEAAAAAA4CAgAAAAAHAQEAAACAg4AAAAAAwEFAAAAAAOAgIAAAAABwEBAAAAAAOAgIAAAAABwEBAAAAAAOAgIAAAAABwEBAAAAgIOAAAAAAMBBQAAAAADgICAAAAAAcBAQAAAAADgICAAAAAAcBAQA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R89sXSS3qfo76bOV+mnnE/TzzifVu5898NJgE3zw4Iu675p3taZ0l8KMS+EmTNd2O00/73JSwN/xAQMG6KyzzmrwvDk5ORo4cKBKS0sPuSYAaAgBAWgG5w3sqA/WFKq0jqsIlX7ptF7RAW2///3vtXr1at18883q3Lmzdu7cKY/HI5/Pp5NOOkmPP/54ved6++23tW3bNt1222265ppr9OabbyrsgHnTt912m8LDw/XCCy9o8ODBjfoMzGVGe/DrbqdoUufj9eXe9aq0fg3r2Fvx7saF6EORGtVF/x70S+30FWrN+nX654xnNW3+M7pu61a5XC4ZYzRw4ED97Gc/0+9+97sWqwMAmuKgk42NMdypCDTCsUlendU/RpHu/b8RNJK8bqM7R3dWdETtv2o9evTQxIkT9e2332rr1q3KycnRr371K3Xv3r3e+wCWLVumK6+8Uq+88opzj8Lll19e67eJ77zzjhYvXtzocCAxlxntR0e3V2fGp+qchKObFA6GDx+u995775DO6S706f+NOluRXq/effdd5efnKy8vTzt27NAjjzyi119/Xb/61a8O6dgA0Nwa+lVhhjFms6R/SJprD+c6K3AEM8boD2O6aGSvaL36Xb52FlUoJdGjK46P15Akr9PvzDPPdH7OyclRSUlJQNuaNWvk8/kC2v7973+rU6dOevbZZ3XPPffohRde0PDhwyVJs2fP1uTJk3Xcccdp+fLlio4OvFJRs76mfBaJuczAgcrKyhq8f6g+X375pYqLi/XII48EtIeFhWnEiBH605/+pPT09OYoEwAO20EDgrX2NGPM0ZKukDTVGDNf0j+stauCUh3QhhhjdHq/GJ3eL6bePk899VSTj7vvt/rR0dGaO3euTjpp/1zpiIgIzZw5U+vWras3HEjMZQZCbdiwYYqOjtZ1112nG264QcnJyXK73SouLtYXX3yhO++8U//v//2/UJcJAJIacQ+CtXalpDtM1a8Vz5R0nzGmu7X29BavDjjCDBw4UFLVDcF//etfNXv2bGVnZ8vvr3qYWr9+/XT++efr97//fa2biy+99FJJ0tKlS1VUVKQxY8Y42/r27RukTwC0bxdeeOFBlwL+4IMP6nyeQXx8vJYsWaKHHnpIF154oTZs2CBrrbxerwYNGqRLL71U1157bUuWDgCN1pS7EUdK+qmk/pLeapFqgHbi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SdfWsV+tvgDQFvl359W7zYS55c/fLbXBgAAAOLJxXRgAWoh7QKpkTJ3brM/X6HsQAAAIJgICALSQmIsukcIjam+IiJD31DFyxcbX3gYAQIgREACghYQPSFXsLXfLeCNlIqNkvJFSRIQ8x5+s2BtuD3V5AADUKVg3KQNAuxR52jh5h56qsq++lC0uUvjAIXJ37xnqslrcrl27dOedd+r5558PdSkAgCbiCgIAtDDj8ch7yihFnj6+VYWD22+/XW63O+BljKnVdskllwTst2PHDsXExNR6uVwuLV68WFLVw5b++c9/1nvu1NRUeb3eel/GGOXl1X+TNwCg5RAQAKCdeuihh1RRUeG8nnjiCYWFhWnKlCkB7f/6178C9uvSpYsKCwtrvXr1avxN11lZWSotLa3zVVBQIEly8XwFBFFubq6GDBlySPvOnDlT48ePb+aKgNDhX18AaMestVq4cKEmTZqkt956SytXrlR2drbGjx+v+fPny+/319qnvLxcmZmZtV6ldT3z4RBrkqTw8PBmOR6wZ8+eeq9UrV27VpLk8/n0/fff13uMzMzMQwoQXC1DW8Q9CADQDuXn5+tXv/qV1qxZo+OOO07XX3+9xo4dK0l644039NFHH+mvf/2rrrjiCg0ePFhPPfWUkpOTJUl5eXkaN26cLrroooBjjhw5UomJic77srIyeb1eSdL69euVlJTUqNp8Pp8kyePxHO7HBCRJsbGxtQLsl19+qbPPPlt9+vRp0XNnZWXVu628vFwej4erZWh1CAgAcASwPp9KFy9Q+XfL5YrpqMhxZ8t9VJ96+8fFxem5555T586d69x++umn6/TTT1dJSYm+/fZbJxzUNHv27IPW5PF4DumqQklJiTwej9xu/hOFlvPyyy/r/PPPb/SX831T7poTV8vQWvGvLwC0cZW5u5R727XyF+yRSkuksDAV/e81RZ33E3W84uo69zmUL9/r169Xjx496t3u9/u1c+dORUTU8eyHJigoKFBcXNxhHQNHHuv3q/zrpSr76ksZj1fekeMU3qf/IR3rm2++0QsvvKClS5fW2maqH264bt26gKsLmzdv1ubNm+X3++VyubRw4UJt2rRJkvTFF18cUh1cLUNrRUAAgDYu/6F75c/dKVVWVjVUVkqVlSrJmC3PkOPlOWl4rX3q+02oMUYbN25Uz54Nr7a0b/70vi9UXq9X3bt317333qthw4bVe/zG2te3sfXgyOUvLlLeXTeqcvNG2dISyeVS0Zv/VuS4c9Txt7c26c/VunXrdN555+mee+7R4MGDa23f96X9wBCdmZmpwsJCffbZZxo5cqSWL1+u5cuXS5JWr16tmJiYJn8urpahteJPJACE2G9+8xv95S9/UadOnZq039SpU7Vl3Vr9sXDz/nBQgy0rVdGb/64zINRl33SHum5Mrqlr165O3/rk5eXp2muvrfccNeXk5GjgwIHNdpMzjjwFTz+iig3rpOov7/L7pfIylWR+oIhBxyjy9MatIDRv3jxdfPHFuuyyy3T33XfX2aeuL+u5ubnKyMjQXXfdpRkzZmjkyJG68cYbne0zZ87Uv//976Z/Lq6WoZXirhgAaEGDBw+ud+WSXbt2SZL++c9/qrCw0NknJyfH+c28MUbjxo0LeP/WW285fW1JsYy79vzlkR8vU593F6n7g08edOWUsrIyPfDAAxo8eLC6deumXr16adiwYUpNTdXdd9+t/Pz8ej+bz+fTjBkzNGLECCUkJCghIUFxcXE65phj9Je//KXeL2BAU/iLi1T62af7w0FNZaUqeuPVBo/x9ddf6+KLL9Z5552n++67T48//niTarj55pt12WWX6Z577tG3336rWbNmNbhPzb+z9b0GDBig7du3O+/3TVkCQo0rCADQgupaNrGkpERRUVH1ztXv06dPwG/aO3bsqMWLF2vQoEG1+rqiomULdtdqXzjuJMkYRQwdoYR7HwrYVnPllKuuukp5eXl6++231b///vncmzdv1j333KMJEybo888/r7POK664Qhs2bNCMGTM0dOhQhYWFSaqabjF9+nSdeuqpWrFixWHfk4D2zZ+fJxMWJltHPpCkyl07GjzGzJkzVVBQoKVLl9b590iSIiMj9bOf/axW+/PPP68vvvhCy5YtU2RkpF555RVNnDhRRx11lEaOHFnvOblahraMgAAAQZafny9jjKKiohrsW1BQoMLCQq1evbrOLzbGG6mIPieo/JvlUsUB36AiPIq56JJa+9RcOeW9997T7NmzA8KBJPXo0UP33nuv+vXrp6KiIkVHR9c6TkZGht58800NHx44hWnAgAF64oknFB0drVWrVtU5zxtoLFd8oqy/9hS6fcKSujZ4jBkzZkiquvfm+eef16uvvqrs7GwVFxersrJS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",
      "text/plain": [
       "<Figure size 1008x720 with 2 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "def drawGraph():\n",
    "    \n",
    "    plt.figure(figsize=(14,10))\n",
    "    plt.scatter(data_result['인구수'], data_result['소계'], s=50, c=data_result['오차'], cmap=my_cmap )\n",
    "    plt.plot(fx, f1(fx), ls='dashed', lw=3, color='g')\n",
    "    \n",
    "    for n in range(5):\n",
    "        # 상위 5개\n",
    "         plt.text(\n",
    "             df_sort_f['인구수'][n]*1.02, # x 좌표\n",
    "             df_sort_f['소계'][n]*0.98, # y 좌표\n",
    "             df_sort_f.index[n],  # title\n",
    "             fontsize=15\n",
    "        )\n",
    "        # 하위 5개\n",
    "         plt.text(\n",
    "             df_sort_t['인구수'][n]*1.02, # x 좌표\n",
    "             df_sort_t['소계'][n]*0.98, # y 좌표\n",
    "             df_sort_t.index[n],  # title\n",
    "             fontsize=15\n",
    "        )\n",
    "    plt.xlabel('인구수')\n",
    "    plt.ylabel(\"CCTV\")\n",
    "    plt.colorbar()\n",
    "    plt.grid(True)\n",
    "    plt.show()\n",
    "\n",
    "drawGraph()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 272,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>소계</th>\n",
       "      <th>최근증가율</th>\n",
       "      <th>인구수</th>\n",
       "      <th>한국인</th>\n",
       "      <th>외국인</th>\n",
       "      <th>고령자</th>\n",
       "      <th>외국인비율</th>\n",
       "      <th>고령자비율</th>\n",
       "      <th>CCTV비율</th>\n",
       "      <th>오차</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>구별</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>강남구</th>\n",
       "      <td>3238</td>\n",
       "      <td>150.619195</td>\n",
       "      <td>561052</td>\n",
       "      <td>556164</td>\n",
       "      <td>4888</td>\n",
       "      <td>65060</td>\n",
       "      <td>0.871220</td>\n",
       "      <td>11.596073</td>\n",
       "      <td>0.577130</td>\n",
       "      <td>1524.595142</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>양천구</th>\n",
       "      <td>2482</td>\n",
       "      <td>34.671731</td>\n",
       "      <td>475018</td>\n",
       "      <td>471154</td>\n",
       "      <td>3864</td>\n",
       "      <td>55234</td>\n",
       "      <td>0.813443</td>\n",
       "      <td>11.627770</td>\n",
       "      <td>0.522507</td>\n",
       "      <td>887.835545</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>용산구</th>\n",
       "      <td>2096</td>\n",
       "      <td>53.216374</td>\n",
       "      <td>244444</td>\n",
       "      <td>229161</td>\n",
       "      <td>15283</td>\n",
       "      <td>36882</td>\n",
       "      <td>6.252148</td>\n",
       "      <td>15.088118</td>\n",
       "      <td>0.857456</td>\n",
       "      <td>821.403817</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>서초구</th>\n",
       "      <td>2297</td>\n",
       "      <td>63.371266</td>\n",
       "      <td>445401</td>\n",
       "      <td>441102</td>\n",
       "      <td>4299</td>\n",
       "      <td>53205</td>\n",
       "      <td>0.965198</td>\n",
       "      <td>11.945415</td>\n",
       "      <td>0.515715</td>\n",
       "      <td>743.883771</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>은평구</th>\n",
       "      <td>2108</td>\n",
       "      <td>85.237258</td>\n",
       "      <td>491202</td>\n",
       "      <td>486794</td>\n",
       "      <td>4408</td>\n",
       "      <td>74559</td>\n",
       "      <td>0.897390</td>\n",
       "      <td>15.178888</td>\n",
       "      <td>0.429151</td>\n",
       "      <td>491.405033</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "       소계       최근증가율     인구수     한국인    외국인    고령자     외국인비율      고령자비율  \\\n",
       "구별                                                                         \n",
       "강남구  3238  150.619195  561052  556164   4888  65060  0.871220  11.596073   \n",
       "양천구  2482   34.671731  475018  471154   3864  55234  0.813443  11.627770   \n",
       "용산구  2096   53.216374  244444  229161  15283  36882  6.252148  15.088118   \n",
       "서초구  2297   63.371266  445401  441102   4299  53205  0.965198  11.945415   \n",
       "은평구  2108   85.237258  491202  486794   4408  74559  0.897390  15.178888   \n",
       "\n",
       "       CCTV비율           오차  \n",
       "구별                          \n",
       "강남구  0.577130  1524.595142  \n",
       "양천구  0.522507   887.835545  \n",
       "용산구  0.857456   821.403817  \n",
       "서초구  0.515715   743.883771  \n",
       "은평구  0.429151   491.405033  "
      ]
     },
     "execution_count": 272,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_sort_f.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 273,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "561052"
      ]
     },
     "execution_count": 273,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data_result['인구수'][0]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 274,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "3238"
      ]
     },
     "execution_count": 274,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data_result['소계'][0]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 275,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'강남구'"
      ]
     },
     "execution_count": 275,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data_result.index[0]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 286,
   "metadata": {},
   "outputs": [],
   "source": [
    "data_result.to_csv(\"../solution/01. CCTV_result.csv\", sep=\",\", encoding=\"utf-8\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "interpreter": {
   "hash": "42476d4792887bd98998eaa349505fad824cf18f74b6a075ec3a971c5ff8fbd0"
  },
  "kernelspec": {
   "display_name": "Python 3.9.7 ('base')",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.12"
  },
  "orig_nbformat": 4
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
