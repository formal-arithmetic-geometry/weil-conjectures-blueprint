+++
kind  = "proof"
of    = "lem-trf-finite-tor-amplitude-perfect"
+++
Write $A=A_{E,n}$ for the finite coefficient ring of
[def-trf-coefficient-conventions]: it is a local ring with
maximal ideal $(\varpi_E)$.

*(If.)* Suppose that $C$ is quasi-isomorphic to a bounded
complex $P^\bullet$ of finite free $A$-modules with $P^i=0$ for
$i\notin[a,b]$. For every $A$-module $M$ the derived tensor
$C\otimes_A^LM\cong P^\bullet\otimes_AM$ is concentrated in degrees
$[a,b]$, so that $\operatorname{Tor}_i^A(C,M)=0$ for
$i\notin[a,b]$: in the notation of
[def-weil-finite-tor-amplitude] the complex $C$ has finite Tor
amplitude, and it is perfect in the sense of
[def-trf-categorical-trace] by construction.

*(Only if.)* Suppose that $C$ has finite Tor amplitude, i.e. finite tor dimension in the sense of
[Stacks, Tag 0652](https://stacks.math.columbia.edu/tag/0652)
(Definition 15.68.1, in Section 15.68, Tor dimension).
Each cohomology module $H^i(C)$ is finite by hypothesis, hence
$0$-pseudo-coherent as an $A$-module by
[Stacks, Tag 064T](https://stacks.math.columbia.edu/tag/064T);
since $C$ is bounded it lies in $D^-(A)$, so
[Stacks, Tag 066B](https://stacks.math.columbia.edu/tag/066B)
shows that the complex $C$ itself is pseudo-coherent. By
[Stacks, Tag 0658](https://stacks.math.columbia.edu/tag/0658) a
pseudo-coherent complex of finite tor dimension over a ring is
perfect, and if it has tor amplitude in $[a,b]$ it is
quasi-isomorphic to a complex $E^\bullet$ of finite projective
$A$-modules with $E^i=0$ for $i\notin[a,b]$. Since $A$ is a
local ring, a finite projective $A$-module is free
([Stacks, Tag 00NZ](https://stacks.math.columbia.edu/tag/00NZ),
Lemma 10.78.5: a finite flat module over a local ring is finite free;
equivalently
[Tag 00NX](https://stacks.math.columbia.edu/tag/00NX), Lemma 10.78.2,
parts (2) and (5), together with Nakayama's lemma), so that
$E^\bullet$ is a bounded
complex of finitely generated free $A$-modules quasi-isomorphic to
$C$: $C$ lies in the category $D^b_{\mathrm{fin}}(A)$ of
[def-trf-categorical-trace].

The finite-Tor-amplitude hypothesis cannot be dropped in the second
direction: the module $A/(\varpi_E)$, viewed as a complex
concentrated in degree $0$, has finite cohomology modules, while its
minimal free resolution

$$
\cdots\to A\xrightarrow{\varpi_E}A\xrightarrow{\varpi_E}A\to
A/(\varpi_E)\to0
$$

is infinite, so that $\operatorname{Tor}_i^A(A/(\varpi_E), A/(\varpi_E))\cong A/(\varpi_E)\neq0$ for all $i\geq0$ and
$A/(\varpi_E)$ is not quasi-isomorphic to a bounded complex of
finite free $A$-modules.

*Recorded in advance* from chapter *The trace formula* of the source.
