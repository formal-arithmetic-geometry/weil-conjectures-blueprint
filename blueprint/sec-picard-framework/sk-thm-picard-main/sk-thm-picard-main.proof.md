+++
kind  = "proof"
of    = "sk-thm-picard-main"
+++
A proper curve over a field is projective (it is quasi-projective, and
proper quasi-projective schemes over a field are projective), so $X$ is a
smooth projective curve. There is a $k$-rational point $\sigma$
([sk-prop-picard-dense-points]).
By [sk-prop-picard-pic-split] it suffices to represent
$G:=\Pic_{X/k,\sigma}$. We verify the conditions of
[sk-thm-picard-criterion]: (1) $G$ is an fppf, hence Zariski, sheaf with small values
([sk-cor-picard-pic-sheaf]); (2)(a) $F$ is representable
([sk-thm-picard-f-representable], applied to the scheme
$\underline{\Hilb}^g_{X/k}$ representing $\Hilb^g_{X/k}$); (2)(b) $F\subseteq G$ is representable
by open immersions ([sk-lem-picard-f-open]); (2)(c) given
$\cL\in G(K)$, [sk-thm-picard-twist] supplies $\cL_0\in G(k)$ with
$h^0=1$ and $H^1=0$ for $\cL_0|_K\otimes\cL$, hence
$Rf_{K,*}(\cL_0|_K\otimes\cL)\cong K[0]$, i.e. $\cL_0\cdot\cL\in F(K)$.
The criterion gives the result, the group structure being the one of
[sk-prop-picard-pic-split].
