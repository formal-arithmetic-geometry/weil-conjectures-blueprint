+++
id = "def-sbc-smooth-morphisms"
kind = "definition"
title = "Smooth morphisms"
order = 5102
lean = ["AlgebraicGeometry.IsSmooth", "AlgebraicGeometry.IsEtale"]
+++
A morphism of schemes $f:X\to Y$ is *smooth* if it is locally of finite
presentation and formally smooth, the latter meaning that every morphism
$T\to X$ over $Y$ from a closed subscheme $T\subset T'$ defined by a
nilpotent ideal sheaf extends, Zariski-locally on $T'$, to a morphism
$T'\to X$ over $Y$ ([Stacks Project, Definition
37.11.1](https://stacks.math.columbia.edu/tag/02H0)); by [Lemma
37.11.7](https://stacks.math.columbia.edu/tag/02H6) this is the notion of a
smooth morphism of [Stacks Project, Section
29.35](https://stacks.math.columbia.edu/tag/01V4).

The description of smooth morphisms by flatness and smooth fibres is the
criterion [sbc-lem-smooth-criterion] stated below. A smooth morphism has
*relative dimension $n$ at a point* if the fibre through that point has
dimension $n$, and *relative dimension $n$* if this holds at every point;
the local constancy of this function is a consequence of that criterion, and
is recorded as [sbc-lem-smooth-relative-dimension-locally-constant]. An
*étale* morphism is a smooth morphism of relative dimension zero.

*Import note.* The source text of this definition contains two lines
duplicated by the LaTeX-to-text conversion ("smooth morphisms by flatness and
smooth fibres is" and "being"), with the sentence about relative dimension
broken across them. The wording above restores the intended sentences.

Unresolved dependencies: def:weil-pbc-scheme-conventions
