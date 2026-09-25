+++
id = "lem-rs-connectivity-reduction"
kind = "lemma"
title = "Openness of the inverse image of the identity component"
order = 2807
uses = ["def-sbc-normal-dominant-galois", "def-weil-pbc-scheme-conventions", "def-wf-algebraic-components", "def-wf-fundamental-representation", "def-wf-geometric-monodromy-group", "def-wf-geometric-semisimplicity", "def-wf-weil-group"]
+++
Let $X_0$ be a normal,
separated finite-type
$k_0$-scheme with $X=X_0\times_{k_0}k$ connected, let
$\mathcal F$ be a lisse $\overline{\mathbf Q}_\ell$-Weil sheaf on
$X_0$ with
fundamental
representation $(V,\rho)$, where $\rho$ is
geometrically semisimple.
With $\Pi:=\pi_1(X,\bar x)$, the geometric subgroup of the
Weil group, $H:=H_{\mathrm{geom}}$ the
geometric monodromy
group (the Zariski closure of $\rho(\Pi)$ in
$\operatorname{GL}(V)$), and $H^\circ$ the identity component of
[def-wf-algebraic-components], put

$$
\Pi^\circ:=\{\gamma\in\Pi:\rho(\gamma)\in H^\circ\}
=\rho^{-1}\bigl(H^\circ\cap\rho(\Pi)\bigr).
$$

Then $\Pi^\circ\triangleleft\Pi$ is a normal subgroup of finite
index, $[\Pi:\Pi^\circ]\le|\pi_0(H)|$, hence open in the profinite
group $\Pi$.

## Proof

The composite

$$
\Pi\xrightarrow{\;\rho\;}
H(\overline{\mathbf Q}_\ell)
\longrightarrow\pi_0(H)
$$

is a group homomorphism into the finite component group
$\pi_0(H)$ of [def-wf-algebraic-components], and its kernel is
exactly $\Pi^\circ$. The component $H^\circ$ is open and closed in
the Zariski topology and hence in the $\ell$-adic topology. Thus the
component map is continuous with finite discrete target, so its kernel
$\Pi^\circ$ is open and normal. Its index is the order of the image,
at most $|\pi_0(H)|$.
