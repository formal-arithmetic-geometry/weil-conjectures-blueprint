+++
id = "def-nagata-common-modification"
kind = "definition"
title = "Common-modification construction"
order = 239
lean = ["AlgebraicGeometry.CommonModification"]
uses = ["def-nagata-admissible-blowup", "def-nagata-elimination-indeterminacy", "def-nagata-extended-admissible-blowup", "def-nagata-global-blowup", "def-nagata-scheme-theoretic-image", "prop-nagata-global-blowup-cover-independent"]
+++
Let $s_i\colon X_i\to S$ ($i=1,2$) be morphisms of schemes and let
$j_i\colon U\hookrightarrow X_i$ be open immersions. A *common
modification* $\mathsf{CM}(X_1,X_2;U)$ of $X_1$ and $X_2$ along $U$
consists of

* $U$-admissible blow-ups $\pi_i\colon X'_i\to X_i$ (admissible with
  respect to the open $j_i(U)\subseteq X_i$), for $i=1,2$;
* a scheme $W$ with a morphism $w\colon W\to S$;
* open immersions $k_i\colon X'_i\to W$ with $w\circ k_i=s_i\circ\pi_i$;
* morphisms $u_i\colon U\to X'_i$ with $\pi_i\circ u_i=j_i$;

such that $k_1\circ u_1=k_2\circ u_2$, the images of $k_1$ and $k_2$ cover
$W$, and $w\colon W\to S$ is separated and of finite type.
