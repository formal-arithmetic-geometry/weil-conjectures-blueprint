+++
id = "def-trf-coefficient-pushforward"
kind = "definition"
title = "Coefficient pushforward of a correspondence"
order = 2451
uses = ["def-trf-admissibility", "def-trf-correspondence"]
+++
Let $f:X\to Y$ be proper, let $c=(c_1,c_2):C\to X\times_sX$ and
$b=(b_1,b_2):D\to Y\times_sY$ be
admissible correspondences, and let
$g:C\to D$ satisfy $b_ig=fc_i$ for $i=1,2$. For
$K\in D^b_{ctf}(X,A)$ put $K'=Rf_*K$. The *coefficient
pushforward* of a coefficient map $u:c_2^*K\to c_1^!K$ is the
composite

$$
[f,g]_!u:b_2^*K'\longrightarrow b_1^!K'
$$

obtained as follows. First, the equality $b_2g=fc_2$ and the proper
base change $Rg_*c_2^*\cong b_2^*Rf_*$ for the Cartesian square
$(c_2,g,b_2,f)$ give $b_2^*K'=b_2^*Rf_*K\cong Rg_*c_2^*K$. Compose
the $Rg_*$-image of $u$ with the exchange map of
[def-trf-admissibility],

$$
Rg_*c_1^!K\longrightarrow b_1^!Rf_*K=b_1^!K',
$$

whose exceptional adjoint is the exchange isomorphism attached to the
Cartesian square $(c_1,g,b_1,f)$ by [def-trf-admissibility].
This is the map of Varshavsky, loc. cit., 1.2.4, formed from the
ordinary units and the exceptional counits.
