+++
id = "def-fd-additive-character"
kind = "definition"
title = "Additive characters"
order = 3925
lean = ["AddChar.FiniteField.primitiveChar"]
uses = ["def-weil-pbc-scheme-conventions"]
+++
Let $k$ be a finite field or an algebraic closure of one, and let
$p=\operatorname{char}k$. A *nondegenerate additive character*
of $k$ is a nontrivial homomorphism

$$
\psi:(k,+)\longrightarrow\overline{\mathbf Q}_\ell^\times.
$$

For a finite field $k_0=\mathbf F_q$ with trace
$\operatorname{Tr}:k_0\to\mathbf F_p$, let $F'$ be a field of
characteristic different from $p$ (for instance
$\overline{\mathbf Q}_\ell$), and fix a nontrivial character
$\Psi:\mathbf F_p\to F'(\mu_p)^\times$ with values in the $p$-th
cyclotomic extension $F'(\mu_p)$ of $F'$. The character
$\psi(x)=\Psi(\operatorname{Tr}(x))$ is called *the* nondegenerate
additive character of $k_0$. It is primitive: for every $a\in k_0^\times$
the scaling $\psi_a(x)=\psi(ax)$ is again nontrivial.
