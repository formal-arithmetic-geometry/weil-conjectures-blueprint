+++
id = "nagata-compactification"
kind = "section"
title = "Nagata compactification"
order = 135
+++
This chapter gives a formalization blueprint for Nagata's compactification
theorem for schemes. The key result is

1. the theorem labelled `thm:nagata-compactification`, asserting
that every separated
finite type morphism $X\to S$ with $S$ quasi-compact and quasi-separated
factors as a quasi-compact open immersion followed by a proper morphism.

The proof follows the scheme-theoretic proof in the Stacks Project. The
intermediate statements are deliberately finer than the printed proof: every
change of ambient scheme, every use of a scheme-theoretic image, every
admissible blow-up, and every valuative lifting step is given its own labelled
interface. This is the level at which the objects and equalities will have to
be supplied to Lean.

Throughout this chapter, ``finite type'' includes quasi-compactness, and a
compactification always has a quasi-compact open immersion as its first map.
Fiber products and all morphisms are taken in the category of schemes.
The current Mathlib interfaces used without a blueprint definition include
rings, ideals, modules, localizations, schemes, fibre products, open and closed
immersions, proper morphisms, finite-presentation morphisms, directed systems,
scheme gluing via `AlgebraicGeometry.Scheme.GlueData.glued`, and
categorical limits. Important verified declarations are recorded in the
implementation notes: `Scheme.Hom.image`, `Scheme.Hom.imageι`,
`Scheme.Hom.toImage`, `Scheme.Hom.toImage_imageι`, the affine
`Proj` charts (`AlgebraicGeometry.Proj.basicOpenIsoSpec` and
`AlgebraicGeometry.Proj.affineOpenCover`), Rees-algebra operations such
as `reesAlgebra` and `reesAlgebra.fg`, and properness stability
and target-locality from `AlgebraicGeometry.IsProper`. Relative Proj,
geometric blow-ups,
flattening by blow-up, and the Noetherian approximation package are not
assumed to exist: each is defined below only as a blueprint interface and is
marked with an explicit gap until its construction is supplied.

Every other named construction used below has a labelled definition. A
statement is written in ordinary mathematical language; a `\lean{...}` name is
an implementation note, not part of the statement. Canonical comparison maps
between chosen closed subschemes are written as isomorphisms unless a chosen
equality has explicitly been fixed.
