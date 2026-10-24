+++
id = "def-tw-eigenvalue"
kind = "definition"
title = "Eigenvalues and their weights"
lean = ["AlgebraicGeometry.WeilGroup.IsOfWeight"]
order = 3805
uses = ["def-tw-conventions", "def-tw-frobenius-action"]
+++
Fix a field embedding $\iota:\overline{\mathbf Q}_\ell\hookrightarrow\mathbf C$.
Let $\alpha\in\overline{\mathbf Q}_\ell$, typically an eigenvalue of the
$\overline{\mathbf Q}_\ell$-linear automorphism $\Phi_X^*$ of
[def-tw-frobenius-action]. Its absolute value is read through $\iota$:

$$
|\alpha|_\iota:=|\iota(\alpha)|,
$$

the complex modulus of $\iota(\alpha)$. For $w\in\mathbf R$, the element
$\alpha$ has *weight* $w$ (relative to $q$ and $\iota$) if

$$
|\iota(\alpha)|=q^{w/2}.
$$

Since $\iota$ is a field embedding, $\iota(q)=q$, so $q$ has weight $2$.
