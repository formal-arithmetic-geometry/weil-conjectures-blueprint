+++
id = "lem-rs-connectivity-cover"
kind = "lemma"
title = "The finite etale cover realising the identity-component subgroup"
order = 2808
uses = ["cor-galois-open-subgroups", "def-sbc-normal-dominant-galois", "def-weil-pbc-scheme-conventions", "def-wf-algebraic-components", "def-wf-fundamental-representation", "def-wf-geometric-monodromy-group", "def-wf-geometric-semisimplicity", "def-wf-weil-group", "lem-rs-connectivity-reduction"]
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

Then there are a connected finite etale cover
$(X',\bar x')\to(X,\bar x)$ and a normal finite-type
$\mathbf F_{q^m}$-scheme $X'_0$ with a finite etale morphism
$X_0'\to X_0^{(m)}=X_0\times_{k_0}\mathbf F_{q^m}$ for some
$m\ge1$ with $X_0'\times_{\mathbf F_{q^m}}k=X'$ and
$\pi_1(X',\bar x')=\Pi^\circ$.

## Proof

By [lem-rs-connectivity-reduction], $\Pi^\circ\triangleleft\Pi$
is open of finite index. By [cor-galois-open-subgroups], the
standard correspondence between open subgroups of the etale fundamental
group of a connected scheme and its connected finite etale covers
(equivalently, the equivalence of finite etale $X$-schemes with
finite continuous $\pi_1$-sets,
[Stacks Project,
Theorem 58.6.2 (1), Tag 0BND](https://stacks.math.columbia.edu/tag/0BND)), $\Pi^\circ$ gives a connected finite
etale cover
$X'\to X$ with $\pi_1(X',\bar x')=\Pi^\circ$. The cover is of
finite presentation over the finite-type scheme $X$, so it descends
to some finite extension of the base field: spreading out the
finite-presentation data over the filtered colimit
$k=\mathrm{colim}_\lambda k_\lambda$ of the finite subfields of
$k$ (standard; EGA IV, Sec. 8.5) gives $m\ge1$ and the finite
etale morphism $X_0'\to X_0^{(m)}$ with
$X_0'\times_{\mathbf F_{q^m}}k=X'$. The field
$\mathbf F_{q^m}$ is a finite
extension of $k_0$. Since $X_0$ is normal, so is its separable
constant-field base change $X_0^{(m)}$; a finite etale algebra over a
normal ring is normal (the local form at each local ring is
[Stacks Project,
Proposition 41.19.7, Tag 025P](https://stacks.math.columbia.edu/tag/025P), for Noetherian local rings, whose proof
appeals to the algebra form, Algebra Lemma 10.163.9), hence $X'_0$ is
normal.
