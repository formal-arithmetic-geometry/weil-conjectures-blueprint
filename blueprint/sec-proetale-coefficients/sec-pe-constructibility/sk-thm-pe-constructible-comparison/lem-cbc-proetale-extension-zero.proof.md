+++
kind  = "proof"
of    = "lem-cbc-proetale-extension-zero"
+++
The exactness and the left-adjoint property are part of
[def-weil-extension-by-zero], which is stated on the pro-etale
site; being exact, $j_!$ acts degreewise on complexes
[def-weil-pbc-derived-categories]. Since $j_!$ and $s^{-1}$ are exact, it
suffices to treat a single sheaf $F$ on $U_{\Proet}$.

If $s=j\circ t$, the square with sides $t$, $\mathrm{id}_T$, $j$ and $s$ is
cartesian because $j$ is a monomorphism. Extension by zero commutes with
pullback along such a cartesian square (both sides are left adjoint to the
same restriction functor), so $s^{-1}j_!F\cong(\mathrm{id}_T)_!t^{-1}F=t^{-1}F$.

If $s(T)\cap U=\emptyset$, the base change $T\times_XU$ is empty. The sheaf
$j_!F$ is the sheafification of the presheaf which on a weakly etale
$X$-scheme $V$ is the sum of the sections of $F$ over the $X$-morphisms
$V\to U$; after pullback to $T$ no object of $T_{\Proet}$ other than the
empty one maps to $U$ over $X$, so $s^{-1}j_!F$ is the initial, that is
the zero, sheaf. For a geometric point $\bar x$ these two cases are the stalk
formula.
