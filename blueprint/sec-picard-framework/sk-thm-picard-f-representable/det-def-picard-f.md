+++
id = "det-def-picard-f"
kind = "definition"
title = "The subfunctor $F$"
order = 810
lean = ["AlgebraicGeometry.picardFunctorInvertibleDirectImage"]
+++
Let $k$ be a field, $X$ a proper $k$-scheme with a $k$-rational point $\sigma$,
and $G:=\Pic_{X/k,\sigma}$. For a $k$-scheme $T$, with $f_T:X_T\to T$,

$$
F(T)=\Bigl\{\cL\in G(T):\ R^0f_{T,*}\cL\ \text{is invertible and }
R^qf_{T,*}\cL=0\text{ for }q>0\Bigr\},
$$

i.e. $Rf_{T,*}\cL$ is isomorphic to an invertible $\cO_T$-module placed in
degree $0$.
