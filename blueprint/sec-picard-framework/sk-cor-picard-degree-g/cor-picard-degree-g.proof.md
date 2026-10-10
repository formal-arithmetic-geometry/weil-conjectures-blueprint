+++
kind  = "proof"
of    = "cor-picard-degree-g"
uses = ["lem-sc-riemann-roch"]
+++
The vanishing gives $\chi(\cL)=h^0(X_K,\cL)=1$
([def-pc-euler-characteristic]), and $\deg\cL=\chi(\cL)-\chi(\cO_{X_K})$
by [def-pc-degree-line-bundle], $X_K$ being proper over $K$. It remains
to compute $\chi(\cO_{X_K})$. Since $\operatorname{Spec}K\to\operatorname{Spec}k$
is flat, cohomology of the quasi-coherent module $\cO_X$ commutes with this
base change: $H^q(X_K,\cO_{X_K})\cong H^q(X,\cO_X)\otimes_kK$ for all $q$,
so $\dim_KH^q(X_K,\cO_{X_K})=\dim_kH^q(X,\cO_X)$. Here $h^0=1$ because
$k\to H^0(X,\cO_X)$ is bijective, $h^1=g$ by definition, and $h^q=0$ for
$q\geq2$ because $X$ is a Noetherian scheme of dimension $1$ (Grothendieck
vanishing). Hence $\chi(\cO_{X_K})=1-g$ and
$\deg\cL=1-(1-g)=g$.
