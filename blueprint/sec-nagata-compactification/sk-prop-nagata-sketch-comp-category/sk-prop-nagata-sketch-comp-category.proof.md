+++
kind  = "proof"
of    = "sk-prop-nagata-sketch-comp-category"
uses = ["sk-lem-nagata-sketch-closure"]
+++
(i) Given $c_1,c_2$, consider

$$
(j_1,j_2):X\longrightarrow\overline X_1\times_S\overline X_2 .
$$

The target is proper over $S$: it is the base change of $\bar f_2$ along
$\bar f_1$, followed by $\bar f_1$. The map is a quasi-compact immersion,
since composing it with the first projection gives the quasi-compact open
immersion $j_1$ while $\overline X_2\to S$ is separated. By
[sk-lem-nagata-sketch-closure] its scheme-theoretic image
$\overline X=\SIm(j_1,j_2)$ is therefore a compactification $c=(j,\bar c)$ of
$f$, where $\bar c:\overline X\to S$ is the restriction of the structure
morphism of $\overline X_1\times_S\overline X_2$ and $j$ is
scheme-theoretically dense.
Each $\overline X_i\to S$ is proper, hence separated, so the projections
$\overline X\to\overline X_i$ are proper; they carry $j$ to $j_i$, and are
thus refinements $c\to c_i$. Induction on the size of the family gives the
finite case.

(ii) Let $u,v:c_1\to c_2$ be parallel refinements and let
$\overline X'\subseteq\overline X_1$ be their equalizer. It is a closed
subscheme, because $\overline X_2\to S$ is proper and hence separated; its
inclusion is therefore a closed immersion, so
$\overline X'\to\overline X_1\xrightarrow{\bar f_1}S$ is proper. And $j_1$
factors through $\overline X'$, because $u\circ j_1=j_2=v\circ j_1$. Hence
$c'=(j_1,\bar f_1|_{\overline X'})$ is an object of
$\operatorname{Comp}(f)$, the inclusion is a refinement $c'\to c_1$, and it
equalizes $u$ and $v$.

*Base change.* Quasi-compact open immersions and proper morphisms are
stable under base change ([sk-lem-nagata-sketch-closure]), which gives the
first two assertions. The construction in (i) uses only fibre products,
scheme-theoretic image and those two stability properties, and
scheme-theoretic image of a quasi-compact morphism commutes with flat base
change and with restriction to an open; so a base-changed common refinement is
again one.
