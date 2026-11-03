+++
id = "lem-kun-0f1d"
kind = "lemma"
title = "Failure of base change produces an integral normal base"
order = 3142
uses = ["def-kun-bc-property", "def-weil-pbc-cartesian-square"]
+++
Let $f:X\to S$ be a morphism of schemes and $n\ge1$ an integer
invertible on $S$ (notation of [def-kun-bc-property]). Assume
that for some $q\ge1$ the property $BC(f,n,q-1)$ holds but
$BC(f,n,q)$ does not. Then there exists a commutative diagram

$$
\begin{array}{ccccc}
X&\longleftarrow&X'&\longleftarrow&Y\\
\Big\downarrow{\scriptstyle f}&&\Big\downarrow{}&&\Big\downarrow{\scriptstyle h}\\
S&\longleftarrow&S'&\longleftarrow&\Spec(K)
\end{array}
$$

with both squares
cartesian, where $S'$ is
affine, integral, and normal with algebraically closed function field
$K$, and an integer $d\mid n$ such that
$R^qh_*(\underline{\mathbf Z/d\mathbf Z})$ is nonzero.
