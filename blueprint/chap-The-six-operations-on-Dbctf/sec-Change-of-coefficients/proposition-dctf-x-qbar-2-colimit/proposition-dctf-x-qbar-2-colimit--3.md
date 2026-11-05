+++
id = "proposition-dctf-x-qbar-2-colimit--3"
kind = "proposition"
title = "Descent of morphisms"
order = 649004
aliases = ["bp-r198-3"]
lean = ["AlgebraicGeometry.ProEtale.constructibleCocone_homInj", "AlgebraicGeometry.ProEtale.constructibleCocone_homSurj"]
+++
Use the scalar extensions of [proposition-dctf-x-qbar-2-colimit--1].

1. Suppose that the underlying topological space of $X$ is noetherian.
   For finite subextensions $E,F\subset\overline{\mathbf Q}_\ell$,
   $K\in D^b_{\mathrm{ctf}}(X,E)$ and $L\in D^b_{\mathrm{ctf}}(X,F)$, every morphism
   $K_{\overline{\mathbf Q}_\ell}\to L_{\overline{\mathbf Q}_\ell}$
   is obtained, using the scalar-extension isomorphisms, from a morphism
   $K_H\to L_H$ for some finite $H$ containing both $E$ and $F$.
2. For any scheme $X$, let $K,L\in D^b_{\mathrm{ctf}}(X,H)$ and let $g,g':K\to L$
   have the same image after extension to $\overline{\mathbf Q}_\ell$.
   There is a finite $H'\supset H$ such that $g_{H'}=g'_{H'}$.

Consequently, when the underlying topological space of $X$ is noetherian
and $K,L\in D^b_{\mathrm{ctf}}(X,E)$, extension of scalars induces a bijection

$$
\varinjlim_{F\supset E}\Hom_{D^b_{\mathrm{ctf}}(X,F)}(K_F,L_F)
\xrightarrow{\sim}\Hom_{D^b_{\mathrm{ctf}}(X,\overline{\mathbf Q}_\ell)}
(K_{\overline{\mathbf Q}_\ell},L_{\overline{\mathbf Q}_\ell}).
$$

The colimit runs over finite subextensions $F\subset\overline{\mathbf Q}_\ell$
containing $E$.
