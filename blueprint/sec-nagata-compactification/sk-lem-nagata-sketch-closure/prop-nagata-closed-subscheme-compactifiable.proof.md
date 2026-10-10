+++
kind  = "proof"
of    = "prop-nagata-closed-subscheme-compactifiable"
+++
Since $X'\to S$ is compactifiable, it has a compactification
$C'=(X'\xrightarrow{j'}\overline X'\xrightarrow{p'}S)$
([def-nagata-compactifiable]); fix any such $C'$ and let
$\mathsf{Closed}(i,C')=(X\to\overline X\to S)$ with
$\overline X=\operatorname{SIm}(j'\circ i)$
([def-nagata-closed-subscheme-compactification]).

The morphism $j'$ is quasi-compact: $p'$ is proper, hence quasi-separated,
and $p'\circ j'=(X'\to S)$ is quasi-compact, so $j'$ is quasi-compact by the
cancellation property of quasi-compact morphisms (the graph argument: $j'$
factors as its graph $X'\to X'\times_S\overline X'$, a base change of the
quasi-compact diagonal of $p'$, followed by the projection to
$\overline X'$, a base change of $X'\to S$). The closed immersion $i$ is
quasi-compact, so $g=j'\circ i\colon X\to\overline X'$ is quasi-compact.

The ambient scheme $\overline X$ is closed in the proper scheme
$\overline X'$, hence is proper over $S$. By
[lemma-nagata-scheme-image-restrict-open] applied to $g$ and the open
$X'\subseteq\overline X'$, the pullback
$\overline X\times_{\overline X'}X'$ is the scheme-theoretic image of the
base change of $g$ to $X'$, which is $i\colon X\hookrightarrow X'$. By
[lemma-nagata-scheme-image-of-closed-immersion], the factor map for $i$ is
an isomorphism, and compatibility with the image inclusion identifies this
scheme-theoretic image with $X$. Hence

$$
X\cong\overline X\times_{\overline X'}X',
$$

so $X\to\overline X$ is identified with the base change of the open
immersion $j'$ along $\overline X\hookrightarrow\overline X'$, and is an
open immersion. The composite $X\to\overline X\to\overline X'\to S$ equals
$X\xrightarrow{i}X'\to S$, which is the structure morphism of $X$. Thus
$\mathsf{Closed}(i,C')$ is a compactification of $X\to S$
([def-nagata-compactification]), and $X\to S$ is compactifiable.
