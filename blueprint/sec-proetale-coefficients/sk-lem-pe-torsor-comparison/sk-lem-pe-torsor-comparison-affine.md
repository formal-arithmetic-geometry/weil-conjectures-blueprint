+++
id = "det-pe-torsor-comparison-affine"
kind = "lemma"
title = "Torsors under a classical group over an affine base"
uses = ["sk-prop-pe-comparison-morphism", "sk-thm-pe-indetale-refinement", "sk-prop-pe-affine-basis", "det-pe-classical-sheaves-image"]
+++
Let $X$ be an affine scheme, $G_0$ a sheaf of groups on $X_{\Et}$ and
$G=\nu_X^*G_0$. Let $T$ be a $G$-torsor on $X_{\Proet}$, i.e. a sheaf of sets with
a left $G$-action such that $G\times T\to T\times T$, $(g,t)\mapsto(gt,t)$, is an
isomorphism and $T\to *$ is an epimorphism. Then there are an affine étale
surjection $U_i\to X$, a $G_0$-torsor $T_0$ on $X_{\Et}$ with $T_0(U_i)\neq\emptyset$,
and an isomorphism of $G$-torsors $\nu_X^*T_0\cong T$. In particular $T$ is
classical and is trivialized by the étale covering $\{U_i\to X\}$.
