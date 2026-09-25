+++
id = "lem-wf-no-central-torus"
kind = "lemma"
title = "No central torus in geometrically semisimple monodromy"
order = 2854
uses = ["def-sbc-normal-dominant-galois", "def-weil-pbc-scheme-conventions", "def-wf-algebraic-torus", "def-wf-geometric-monodromy-group", "def-wf-geometric-semisimplicity", "lem-wf-central-weight-determinant-character", "lem-wf-faithful-semisimple-reductive", "lem-wf-geometric-closure-semisimple", "lem-wf-invariant-character-extension", "lem-wf-reductive-connected-centre", "lem-wf-torus-central-power-trivial", "thm-wf-rank-one-finite-geometric-image-curve"]
+++
Let $X_0$ be a
normal, geometrically connected
separated finite-type scheme
of pure dimension one over a finite field. Assume that $\rho$
is geometrically semisimple and that $H=H_{\mathrm{geom}}$ is connected.
Then $Z(H)^\circ=1$.

## Proof

By [lem-wf-geometric-closure-semisimple] and
[lem-wf-faithful-semisimple-reductive], $H$ is reductive, and
$T=Z(H)^\circ$ is a torus by
[lem-wf-reductive-connected-centre]. Suppose that $T\ne1$.
Choose a degree-one lift $s$ and put $\zeta=\rho(s)$. By
[lem-wf-torus-central-power-trivial], conjugation by $\zeta^m$
is the identity on $T$ for some $m>0$. The determinant construction
of [lem-wf-central-weight-determinant-character] gives a
non-trivial algebraic character $\chi:H\to\mathbf G_m$ satisfying
$\chi\circ\operatorname{Int}(\zeta^m)=\chi$. By
[lem-wf-invariant-character-extension], after the constant-field
extension of degree $m$, the geometric character
$\chi\circ\rho|_{\pi_1(X)}$ is the restriction of a rank-one Weil
character $\widetilde\chi$.

The rank-one finiteness statement
[thm-wf-rank-one-finite-geometric-image-curve] now says that
$\chi(\rho(\pi_1(X)))$ is finite. Its Zariski closure is therefore
finite. On the other hand $\rho(\pi_1(X))$ is Zariski dense in $H$
by [def-wf-geometric-monodromy-group], and continuity of the
algebraic map $\chi$ gives

$$
\chi(H)=\chi\bigl(\overline{\rho(\pi_1(X))}\bigr)
\subseteq\overline{\chi(\rho(\pi_1(X)))} .
$$

Moreover $\chi|_T$ is a non-trivial monomial on the split torus
$T\cong\mathbf G_m^d$, hence is surjective over the algebraically
closed field $\Qlb$. Thus $\chi(H)\supseteq\chi(T)=\mathbf G_m$, so the Zariski
closure of $\chi(\rho(\pi_1(X)))$ is all of $\mathbf G_m$, while it
is also finite by the previous paragraph: a contradiction. Hence
$T=1$.
