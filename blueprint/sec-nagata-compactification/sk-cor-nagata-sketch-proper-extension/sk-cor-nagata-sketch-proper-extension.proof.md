+++
kind  = "proof"
of    = "sk-cor-nagata-sketch-proper-extension"
uses = ["sk-thm-nagata-sketch-conrad"]
+++
Replace $Y$ by $Y\times_SX$: then $f$ becomes a section over $U$ of the
proper morphism $Y\times_SX\to X$, with closed image over $U$ because that
morphism is separated. Apply [sk-thm-nagata-sketch-conrad] with $V=U$. The
resulting partial extension $g\colon W\to Y\times_SX$ on an open
$W\supseteq\pi^{-1}(U)$ of $X'$ has closed graph in
$(Y\times_SX)\times_XX'$, which is proper over $X'$; so $W\to X'$ is both
proper and an open immersion. Its image is dense, hence all of $X'$, and
$g$ followed by the projection to $Y$ is the required $S$-morphism.
