+++
id = "det-tf-contracting-restricted-morphism"
kind = "lemma"
title = "The restricted coefficient morphism"
uses = ["def-trf-correspondence"]
+++
Let $c=(c_1,c_2):C\to X\times X$ be a correspondence of separated finite-type schemes over an
algebraically closed field $k$, let $Z\subset X$ have ideal $I$, and assume
$c_2^\cdot I\,\mathcal O_C\subset c_1^\cdot I\,\mathcal O_C$. Put
$C_Z=(c_1^{-1}Z)_{\mathrm{red}}$ with closed immersion $e:C_Z\hookrightarrow C$, let
$i:Z_{\mathrm{red}}\hookrightarrow X$, and let $c_{Z,1},c_{Z,2}:C_Z\to Z_{\mathrm{red}}$ be the
maps induced by the two legs. Then:

1. **(1)** $c_2$ maps $C_Z$ into $Z_{\mathrm{red}}$, so $c_{Z,2}$ is defined and
   $e^*c_2^*K\simeq c_{Z,2}^*i^*K$;
2. **(2)** compact-support base change and nilpotent invariance give
   $i^*Rc_{1!}\simeq Rc_{Z,1!}e^*$.

For $K\in\Dctf(X,A)$ and $u:c_2^*K\to c_1^!K$ with adjoint
$\widehat u:Rc_{1!}c_2^*K\to K$, the *restricted morphism*
$u_Z:c_{Z,2}^*i^*K\to c_{Z,1}^!i^*K$ is the $Rc_{Z,1!}\dashv c_{Z,1}^!$-adjoint of

$$
 Rc_{Z,1!}c_{Z,2}^*i^*K\simeq i^*Rc_{1!}c_2^*K\xrightarrow{i^*\widehat u}i^*K.
$$

Equivalently, $u_Z$ is $e^*u$ followed by the base-change mate
$e^*c_1^!K\to c_{Z,1}^!i^*K$.
