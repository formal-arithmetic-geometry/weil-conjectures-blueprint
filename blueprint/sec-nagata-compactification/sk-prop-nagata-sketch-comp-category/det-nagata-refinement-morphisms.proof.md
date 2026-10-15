+++
kind  = "proof"
of    = "det-nagata-refinement-morphisms"
uses = ["lemma-nagata-ext-scheme-theoretically-dominant-separated"]
+++
*Properness.* Factor $h$ as the graph
$\Gamma_h:\overline X'\to\overline X'\times_S\overline X$ followed by the
second projection. Since $p:\overline X\to S$ is proper, hence separated,
$\Gamma_h$ is a closed immersion, hence proper; the second projection is the
base change of the proper morphism $p'$ along $p$, hence proper. So $h$ is
proper.

*Inverse image of $X$.* Put $V=h^{-1}(j(X))$, an open subscheme of
$\overline X'$ containing $j'(X)$ because $hj'=j$. Let
$g=j^{-1}\circ h|_V:V\to X$. Then $g\circ j'=\mathrm{id}_X$, so
$j':X\to V$ is a section of $g$. The composite $V\to X\to S$ is the
restriction of $p'$ to the open $V$, which is separated; hence $g$ is
separated (if a composite $V\to X\to S$ is separated, so is $V\to X$). A
section of a separated morphism is a closed immersion, so $j'(X)$ is closed in
$V$; it is also open. Write $V=j'(X)\sqcup V''$ with $V''$ open and closed in
$V$. Restricting the injective map $\mathcal O_{\overline X'}\to
j'_*\mathcal O_X$ (density of $c'$) to the open $V''$ gives an injective map
$\mathcal O_{V''}\to 0$, because $j'(X)\cap V''=\varnothing$. Hence
$\mathcal O_{V''}=0$, i.e. $V''=\varnothing$, and $V=j'(X)$.

*Uniqueness.* If $h_1,h_2:\overline X'\to\overline X$ are $S$-morphisms with
$h_1j'=j=h_2j'$, they agree on the scheme-theoretically dense open
$j'(X)$, and $\overline X\to S$ is separated; by
[lemma-nagata-ext-scheme-theoretically-dominant-separated] $h_1=h_2$.
