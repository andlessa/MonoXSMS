# This file was automatically created by FeynRules 2.3.7
# Mathematica version: 9.0 for Linux x86 (64-bit) (November 20, 2012)
# Date: Mon 24 Aug 2015 14:17:58


from object_library import all_vertices, all_CTvertices, Vertex, CTVertex
import particles as P
import CT_couplings as C
import lorentz as L


V_1 = CTVertex(name = 'V_1',
               type = 'R2',
               particles = [ P.t__tilde__, P.t, P.Y0 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS4, L.FFS6 ],
               loop_particles = [ [ [P.g, P.t] ] ],
               couplings = {(0,0,0):C.R2GC_219_69,(0,1,0):C.R2GC_220_70})

V_2 = CTVertex(name = 'V_2',
               type = 'R2',
               particles = [ P.g, P.g, P.g ],
               color = [ 'f(1,2,3)' ],
               lorentz = [ L.VVV1, L.VVV2 ],
               loop_particles = [ [ [P.b], [P.c], [P.d], [P.s], [P.t], [P.u] ], [ [P.g] ] ],
               couplings = {(0,0,0):C.R2GC_201_56,(0,1,1):C.R2GC_124_1})

V_3 = CTVertex(name = 'V_3',
               type = 'R2',
               particles = [ P.g, P.g, P.g, P.g ],
               color = [ 'd(-1,1,3)*d(-1,2,4)', 'd(-1,1,3)*f(-1,2,4)', 'd(-1,1,4)*d(-1,2,3)', 'd(-1,1,4)*f(-1,2,3)', 'd(-1,2,3)*f(-1,1,4)', 'd(-1,2,4)*f(-1,1,3)', 'f(-1,1,2)*f(-1,3,4)', 'f(-1,1,3)*f(-1,2,4)', 'f(-1,1,4)*f(-1,2,3)', 'Identity(1,2)*Identity(3,4)', 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
               lorentz = [ L.VVVV10, L.VVVV2, L.VVVV3, L.VVVV5 ],
               loop_particles = [ [ [P.b], [P.c], [P.d], [P.s], [P.t], [P.u] ], [ [P.g] ] ],
               couplings = {(2,1,0):C.R2GC_166_35,(2,1,1):C.R2GC_166_36,(0,1,0):C.R2GC_166_35,(0,1,1):C.R2GC_166_36,(4,1,0):C.R2GC_164_31,(4,1,1):C.R2GC_164_32,(3,1,0):C.R2GC_164_31,(3,1,1):C.R2GC_164_32,(8,1,0):C.R2GC_165_33,(8,1,1):C.R2GC_165_34,(7,1,0):C.R2GC_170_41,(7,1,1):C.R2GC_205_61,(6,1,0):C.R2GC_169_40,(6,1,1):C.R2GC_206_62,(5,1,0):C.R2GC_164_31,(5,1,1):C.R2GC_164_32,(1,1,0):C.R2GC_164_31,(1,1,1):C.R2GC_164_32,(11,0,0):C.R2GC_168_38,(11,0,1):C.R2GC_168_39,(10,0,0):C.R2GC_168_38,(10,0,1):C.R2GC_168_39,(9,0,1):C.R2GC_167_37,(2,2,0):C.R2GC_166_35,(2,2,1):C.R2GC_166_36,(0,2,0):C.R2GC_166_35,(0,2,1):C.R2GC_166_36,(6,2,0):C.R2GC_202_57,(6,2,1):C.R2GC_202_58,(4,2,0):C.R2GC_164_31,(4,2,1):C.R2GC_164_32,(3,2,0):C.R2GC_164_31,(3,2,1):C.R2GC_164_32,(8,2,0):C.R2GC_165_33,(8,2,1):C.R2GC_205_61,(7,2,0):C.R2GC_170_41,(7,2,1):C.R2GC_165_34,(5,2,0):C.R2GC_164_31,(5,2,1):C.R2GC_164_32,(1,2,0):C.R2GC_164_31,(1,2,1):C.R2GC_164_32,(2,3,0):C.R2GC_166_35,(2,3,1):C.R2GC_166_36,(0,3,0):C.R2GC_166_35,(0,3,1):C.R2GC_166_36,(4,3,0):C.R2GC_164_31,(4,3,1):C.R2GC_164_32,(3,3,0):C.R2GC_164_31,(3,3,1):C.R2GC_164_32,(8,3,0):C.R2GC_165_33,(8,3,1):C.R2GC_203_60,(6,3,0):C.R2GC_169_40,(7,3,0):C.R2GC_203_59,(7,3,1):C.R2GC_203_60,(5,3,0):C.R2GC_164_31,(5,3,1):C.R2GC_164_32,(1,3,0):C.R2GC_164_31,(1,3,1):C.R2GC_164_32})

V_4 = CTVertex(name = 'V_4',
               type = 'R2',
               particles = [ P.t__tilde__, P.b, P.G__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS5 ],
               loop_particles = [ [ [P.b, P.g, P.t] ] ],
               couplings = {(0,0,0):C.R2GC_215_65})

V_5 = CTVertex(name = 'V_5',
               type = 'R2',
               particles = [ P.t__tilde__, P.t, P.G0 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               loop_particles = [ [ [P.g, P.t] ] ],
               couplings = {(0,0,0):C.R2GC_217_67})

V_6 = CTVertex(name = 'V_6',
               type = 'R2',
               particles = [ P.t__tilde__, P.t, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               loop_particles = [ [ [P.g, P.t] ] ],
               couplings = {(0,0,0):C.R2GC_218_68})

V_7 = CTVertex(name = 'V_7',
               type = 'R2',
               particles = [ P.b__tilde__, P.t, P.G__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3 ],
               loop_particles = [ [ [P.b, P.g, P.t] ] ],
               couplings = {(0,0,0):C.R2GC_216_66})

V_8 = CTVertex(name = 'V_8',
               type = 'R2',
               particles = [ P.u__tilde__, P.u, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               loop_particles = [ [ [P.g, P.u] ] ],
               couplings = {(0,0,0):C.R2GC_132_9})

V_9 = CTVertex(name = 'V_9',
               type = 'R2',
               particles = [ P.c__tilde__, P.c, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               loop_particles = [ [ [P.c, P.g] ] ],
               couplings = {(0,0,0):C.R2GC_132_9})

V_10 = CTVertex(name = 'V_10',
                type = 'R2',
                particles = [ P.t__tilde__, P.t, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_132_9})

V_11 = CTVertex(name = 'V_11',
                type = 'R2',
                particles = [ P.u__tilde__, P.u, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_174_44})

V_12 = CTVertex(name = 'V_12',
                type = 'R2',
                particles = [ P.c__tilde__, P.c, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_174_44})

V_13 = CTVertex(name = 'V_13',
                type = 'R2',
                particles = [ P.t__tilde__, P.t, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_174_44})

V_14 = CTVertex(name = 'V_14',
                type = 'R2',
                particles = [ P.d__tilde__, P.u, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.d, P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_195_49})

V_15 = CTVertex(name = 'V_15',
                type = 'R2',
                particles = [ P.s__tilde__, P.u, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.g, P.s, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_197_51})

V_16 = CTVertex(name = 'V_16',
                type = 'R2',
                particles = [ P.d__tilde__, P.c, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.c, P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_191_45})

V_17 = CTVertex(name = 'V_17',
                type = 'R2',
                particles = [ P.s__tilde__, P.c, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.c, P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_193_47})

V_18 = CTVertex(name = 'V_18',
                type = 'R2',
                particles = [ P.b__tilde__, P.t, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.b, P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_212_64})

V_19 = CTVertex(name = 'V_19',
                type = 'R2',
                particles = [ P.u__tilde__, P.u, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_147_25,(0,1,0):C.R2GC_133_10})

V_20 = CTVertex(name = 'V_20',
                type = 'R2',
                particles = [ P.c__tilde__, P.c, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_147_25,(0,1,0):C.R2GC_133_10})

V_21 = CTVertex(name = 'V_21',
                type = 'R2',
                particles = [ P.t__tilde__, P.t, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_147_25,(0,1,0):C.R2GC_133_10})

V_22 = CTVertex(name = 'V_22',
                type = 'R2',
                particles = [ P.d__tilde__, P.d, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_172_43})

V_23 = CTVertex(name = 'V_23',
                type = 'R2',
                particles = [ P.s__tilde__, P.s, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_172_43})

V_24 = CTVertex(name = 'V_24',
                type = 'R2',
                particles = [ P.b__tilde__, P.b, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_172_43})

V_25 = CTVertex(name = 'V_25',
                type = 'R2',
                particles = [ P.d__tilde__, P.d, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_174_44})

V_26 = CTVertex(name = 'V_26',
                type = 'R2',
                particles = [ P.s__tilde__, P.s, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_174_44})

V_27 = CTVertex(name = 'V_27',
                type = 'R2',
                particles = [ P.b__tilde__, P.b, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_174_44})

V_28 = CTVertex(name = 'V_28',
                type = 'R2',
                particles = [ P.u__tilde__, P.d, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.d, P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_196_50})

V_29 = CTVertex(name = 'V_29',
                type = 'R2',
                particles = [ P.c__tilde__, P.d, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.c, P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_192_46})

V_30 = CTVertex(name = 'V_30',
                type = 'R2',
                particles = [ P.u__tilde__, P.s, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.g, P.s, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_198_52})

V_31 = CTVertex(name = 'V_31',
                type = 'R2',
                particles = [ P.c__tilde__, P.s, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.c, P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_194_48})

V_32 = CTVertex(name = 'V_32',
                type = 'R2',
                particles = [ P.t__tilde__, P.b, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.b, P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_212_64})

V_33 = CTVertex(name = 'V_33',
                type = 'R2',
                particles = [ P.d__tilde__, P.d, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_146_24,(0,1,0):C.R2GC_131_8})

V_34 = CTVertex(name = 'V_34',
                type = 'R2',
                particles = [ P.s__tilde__, P.s, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_146_24,(0,1,0):C.R2GC_131_8})

V_35 = CTVertex(name = 'V_35',
                type = 'R2',
                particles = [ P.b__tilde__, P.b, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_146_24,(0,1,0):C.R2GC_131_8})

V_36 = CTVertex(name = 'V_36',
                type = 'R2',
                particles = [ P.u__tilde__, P.u ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_171_42})

V_37 = CTVertex(name = 'V_37',
                type = 'R2',
                particles = [ P.c__tilde__, P.c ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_171_42})

V_38 = CTVertex(name = 'V_38',
                type = 'R2',
                particles = [ P.t__tilde__, P.t ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF2, L.FF3, L.FF4, L.FF5 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_211_63,(0,2,0):C.R2GC_211_63,(0,1,0):C.R2GC_171_42,(0,3,0):C.R2GC_171_42})

V_39 = CTVertex(name = 'V_39',
                type = 'R2',
                particles = [ P.d__tilde__, P.d ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_171_42})

V_40 = CTVertex(name = 'V_40',
                type = 'R2',
                particles = [ P.s__tilde__, P.s ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_171_42})

V_41 = CTVertex(name = 'V_41',
                type = 'R2',
                particles = [ P.b__tilde__, P.b ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_171_42})

V_42 = CTVertex(name = 'V_42',
                type = 'R2',
                particles = [ P.g, P.g ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VV1, L.VV2, L.VV3 ],
                loop_particles = [ [ [P.b], [P.c], [P.d], [P.s], [P.t], [P.u] ], [ [P.g] ], [ [P.t] ] ],
                couplings = {(0,0,1):C.R2GC_200_55,(0,1,2):C.R2GC_125_2,(0,2,0):C.R2GC_199_53,(0,2,1):C.R2GC_199_54})

V_43 = CTVertex(name = 'V_43',
                type = 'R2',
                particles = [ P.g, P.g, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVS2 ],
                loop_particles = [ [ [P.t] ] ],
                couplings = {(0,0,0):C.R2GC_126_3})

V_44 = CTVertex(name = 'V_44',
                type = 'R2',
                particles = [ P.g, P.g, P.Y0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVS2 ],
                loop_particles = [ [ [P.t] ] ],
                couplings = {(0,0,0):C.R2GC_127_4})

V_45 = CTVertex(name = 'V_45',
                type = 'R2',
                particles = [ P.g, P.g, P.W__minus__, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVVV2, L.VVVV3, L.VVVV5 ],
                loop_particles = [ [ [P.b, P.t] ], [ [P.c, P.d] ], [ [P.c, P.s] ], [ [P.d, P.u] ], [ [P.s, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_151_26,(0,0,1):C.R2GC_151_27,(0,0,2):C.R2GC_151_28,(0,0,3):C.R2GC_151_29,(0,0,4):C.R2GC_151_30,(0,1,0):C.R2GC_151_26,(0,1,1):C.R2GC_151_27,(0,1,2):C.R2GC_151_28,(0,1,3):C.R2GC_151_29,(0,1,4):C.R2GC_151_30,(0,2,0):C.R2GC_151_26,(0,2,1):C.R2GC_151_27,(0,2,2):C.R2GC_151_28,(0,2,3):C.R2GC_151_29,(0,2,4):C.R2GC_151_30})

V_46 = CTVertex(name = 'V_46',
                type = 'R2',
                particles = [ P.a, P.g, P.g, P.Z ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.VVVV2, L.VVVV3, L.VVVV5 ],
                loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_142_16,(0,0,1):C.R2GC_142_17,(0,1,0):C.R2GC_142_16,(0,1,1):C.R2GC_142_17,(0,2,0):C.R2GC_142_16,(0,2,1):C.R2GC_142_17})

V_47 = CTVertex(name = 'V_47',
                type = 'R2',
                particles = [ P.g, P.g, P.Z, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVVV2, L.VVVV3, L.VVVV5 ],
                loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_145_22,(0,0,1):C.R2GC_145_23,(0,1,0):C.R2GC_145_22,(0,1,1):C.R2GC_145_23,(0,2,0):C.R2GC_145_22,(0,2,1):C.R2GC_145_23})

V_48 = CTVertex(name = 'V_48',
                type = 'R2',
                particles = [ P.a, P.a, P.g, P.g ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.VVVV2, L.VVVV3, L.VVVV5 ],
                loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_140_12,(0,0,1):C.R2GC_140_13,(0,1,0):C.R2GC_140_12,(0,1,1):C.R2GC_140_13,(0,2,0):C.R2GC_140_12,(0,2,1):C.R2GC_140_13})

V_49 = CTVertex(name = 'V_49',
                type = 'R2',
                particles = [ P.g, P.g, P.g, P.Z ],
                color = [ 'd(1,2,3)', 'f(1,2,3)' ],
                lorentz = [ L.VVVV1, L.VVVV2, L.VVVV3, L.VVVV5 ],
                loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ] ],
                couplings = {(1,0,0):C.R2GC_144_20,(1,0,1):C.R2GC_144_21,(0,1,0):C.R2GC_143_18,(0,1,1):C.R2GC_143_19,(0,2,0):C.R2GC_143_18,(0,2,1):C.R2GC_143_19,(0,3,0):C.R2GC_143_18,(0,3,1):C.R2GC_143_19})

V_50 = CTVertex(name = 'V_50',
                type = 'R2',
                particles = [ P.a, P.g, P.g, P.g ],
                color = [ 'd(2,3,4)' ],
                lorentz = [ L.VVVV2, L.VVVV3, L.VVVV5 ],
                loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_141_14,(0,0,1):C.R2GC_141_15,(0,1,0):C.R2GC_141_14,(0,1,1):C.R2GC_141_15,(0,2,0):C.R2GC_141_14,(0,2,1):C.R2GC_141_15})

V_51 = CTVertex(name = 'V_51',
                type = 'R2',
                particles = [ P.g, P.g, P.H, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.t] ] ],
                couplings = {(0,0,0):C.R2GC_128_5})

V_52 = CTVertex(name = 'V_52',
                type = 'R2',
                particles = [ P.g, P.g, P.G0, P.G0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.t] ] ],
                couplings = {(0,0,0):C.R2GC_128_5})

V_53 = CTVertex(name = 'V_53',
                type = 'R2',
                particles = [ P.g, P.g, P.G__minus__, P.G__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.b, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_128_5})

V_54 = CTVertex(name = 'V_54',
                type = 'R2',
                particles = [ P.g, P.g, P.H, P.Y0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.t] ] ],
                couplings = {(0,0,0):C.R2GC_130_7})

V_55 = CTVertex(name = 'V_55',
                type = 'R2',
                particles = [ P.g, P.g, P.G0, P.Y0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.t] ] ],
                couplings = {(0,0,0):C.R2GC_129_6})

V_56 = CTVertex(name = 'V_56',
                type = 'R2',
                particles = [ P.g, P.g, P.Y0, P.Y0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.t] ] ],
                couplings = {(0,0,0):C.R2GC_139_11})

V_57 = CTVertex(name = 'V_57',
                type = 'UV',
                particles = [ P.t__tilde__, P.t, P.Y0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS4, L.FFS6 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_219_80,(0,1,0):C.UVGC_220_81})

V_58 = CTVertex(name = 'V_58',
                type = 'UV',
                particles = [ P.g, P.g, P.g ],
                color = [ 'f(1,2,3)' ],
                lorentz = [ L.VVV1, L.VVV3, L.VVV4 ],
                loop_particles = [ [ [P.b], [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.t] ] ],
                couplings = {(0,0,0):C.UVGC_201_44,(0,0,3):C.UVGC_201_45,(0,1,1):C.UVGC_152_1,(0,2,2):C.UVGC_153_2})

V_59 = CTVertex(name = 'V_59',
                type = 'UV',
                particles = [ P.g, P.g, P.g, P.g ],
                color = [ 'd(-1,1,3)*d(-1,2,4)', 'd(-1,1,3)*f(-1,2,4)', 'd(-1,1,4)*d(-1,2,3)', 'd(-1,1,4)*f(-1,2,3)', 'd(-1,2,3)*f(-1,1,4)', 'd(-1,2,4)*f(-1,1,3)', 'f(-1,1,2)*f(-1,3,4)', 'f(-1,1,3)*f(-1,2,4)', 'f(-1,1,4)*f(-1,2,3)', 'Identity(1,2)*Identity(3,4)', 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.VVVV10, L.VVVV2, L.VVVV3, L.VVVV5 ],
                loop_particles = [ [ [P.b], [P.c], [P.d], [P.s], [P.t], [P.u] ], [ [P.b], [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.t] ] ],
                couplings = {(2,1,2):C.UVGC_165_9,(2,1,3):C.UVGC_165_8,(0,1,2):C.UVGC_165_9,(0,1,3):C.UVGC_165_8,(4,1,2):C.UVGC_164_6,(4,1,3):C.UVGC_164_7,(3,1,2):C.UVGC_164_6,(3,1,3):C.UVGC_164_7,(8,1,2):C.UVGC_165_8,(8,1,3):C.UVGC_165_9,(7,1,1):C.UVGC_205_54,(7,1,2):C.UVGC_205_55,(7,1,3):C.UVGC_205_56,(7,1,4):C.UVGC_205_57,(6,1,1):C.UVGC_205_54,(6,1,2):C.UVGC_206_58,(6,1,3):C.UVGC_206_59,(6,1,4):C.UVGC_205_57,(5,1,2):C.UVGC_164_6,(5,1,3):C.UVGC_164_7,(1,1,2):C.UVGC_164_6,(1,1,3):C.UVGC_164_7,(11,0,2):C.UVGC_168_12,(11,0,3):C.UVGC_168_13,(10,0,2):C.UVGC_168_12,(10,0,3):C.UVGC_168_13,(9,0,2):C.UVGC_167_10,(9,0,3):C.UVGC_167_11,(2,2,2):C.UVGC_165_9,(2,2,3):C.UVGC_165_8,(0,2,2):C.UVGC_165_9,(0,2,3):C.UVGC_165_8,(6,2,2):C.UVGC_202_46,(6,2,3):C.UVGC_202_47,(6,2,4):C.UVGC_202_48,(4,2,2):C.UVGC_164_6,(4,2,3):C.UVGC_164_7,(3,2,2):C.UVGC_164_6,(3,2,3):C.UVGC_164_7,(8,2,1):C.UVGC_207_60,(8,2,2):C.UVGC_205_55,(8,2,3):C.UVGC_207_61,(8,2,4):C.UVGC_207_62,(7,2,0):C.UVGC_169_14,(7,2,2):C.UVGC_165_8,(7,2,3):C.UVGC_170_15,(5,2,2):C.UVGC_164_6,(5,2,3):C.UVGC_164_7,(1,2,2):C.UVGC_164_6,(1,2,3):C.UVGC_164_7,(2,3,2):C.UVGC_165_9,(2,3,3):C.UVGC_165_8,(0,3,2):C.UVGC_165_9,(0,3,3):C.UVGC_165_8,(4,3,2):C.UVGC_164_6,(4,3,3):C.UVGC_164_7,(3,3,2):C.UVGC_164_6,(3,3,3):C.UVGC_164_7,(8,3,1):C.UVGC_204_51,(8,3,2):C.UVGC_203_49,(8,3,3):C.UVGC_204_52,(8,3,4):C.UVGC_204_53,(6,3,0):C.UVGC_169_14,(6,3,3):C.UVGC_167_10,(7,3,2):C.UVGC_203_49,(7,3,3):C.UVGC_203_50,(7,3,4):C.UVGC_202_48,(5,3,2):C.UVGC_164_6,(5,3,3):C.UVGC_164_7,(1,3,2):C.UVGC_164_6,(1,3,3):C.UVGC_164_7})

V_60 = CTVertex(name = 'V_60',
                type = 'UV',
                particles = [ P.t__tilde__, P.b, P.G__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS5 ],
                loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.t] ], [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_215_72,(0,0,2):C.UVGC_215_73,(0,0,1):C.UVGC_215_74})

V_61 = CTVertex(name = 'V_61',
                type = 'UV',
                particles = [ P.t__tilde__, P.t, P.G0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS1 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_217_78})

V_62 = CTVertex(name = 'V_62',
                type = 'UV',
                particles = [ P.t__tilde__, P.t, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS2 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_218_79})

V_63 = CTVertex(name = 'V_63',
                type = 'UV',
                particles = [ P.b__tilde__, P.t, P.G__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.t] ], [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_216_75,(0,0,2):C.UVGC_216_76,(0,0,1):C.UVGC_216_77})

V_64 = CTVertex(name = 'V_64',
                type = 'UV',
                particles = [ P.u__tilde__, P.u, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV4 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.UVGC_157_5})

V_65 = CTVertex(name = 'V_65',
                type = 'UV',
                particles = [ P.c__tilde__, P.c, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV4 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.UVGC_157_5})

V_66 = CTVertex(name = 'V_66',
                type = 'UV',
                particles = [ P.t__tilde__, P.t, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_157_5,(0,1,0):C.UVGC_209_64,(0,2,0):C.UVGC_209_64})

V_67 = CTVertex(name = 'V_67',
                type = 'UV',
                particles = [ P.u__tilde__, P.u, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.b], [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.u] ], [ [P.t] ] ],
                couplings = {(0,0,3):C.UVGC_174_23,(0,1,0):C.UVGC_173_18,(0,1,1):C.UVGC_173_19,(0,1,2):C.UVGC_173_20,(0,1,4):C.UVGC_173_21,(0,1,3):C.UVGC_173_22,(0,2,0):C.UVGC_173_18,(0,2,1):C.UVGC_173_19,(0,2,2):C.UVGC_173_20,(0,2,4):C.UVGC_173_21,(0,2,3):C.UVGC_173_22})

V_68 = CTVertex(name = 'V_68',
                type = 'UV',
                particles = [ P.c__tilde__, P.c, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.b], [P.c], [P.d], [P.s], [P.u] ], [ [P.c, P.g] ], [ [P.g] ], [ [P.ghG] ], [ [P.t] ] ],
                couplings = {(0,0,1):C.UVGC_174_23,(0,1,0):C.UVGC_173_18,(0,1,2):C.UVGC_173_19,(0,1,3):C.UVGC_173_20,(0,1,4):C.UVGC_173_21,(0,1,1):C.UVGC_173_22,(0,2,0):C.UVGC_173_18,(0,2,2):C.UVGC_173_19,(0,2,3):C.UVGC_173_20,(0,2,4):C.UVGC_173_21,(0,2,1):C.UVGC_173_22})

V_69 = CTVertex(name = 'V_69',
                type = 'UV',
                particles = [ P.t__tilde__, P.t, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.b], [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.t] ], [ [P.t] ] ],
                couplings = {(0,0,3):C.UVGC_174_23,(0,1,0):C.UVGC_173_18,(0,1,1):C.UVGC_173_19,(0,1,2):C.UVGC_173_20,(0,1,4):C.UVGC_173_21,(0,1,3):C.UVGC_210_65,(0,2,0):C.UVGC_173_18,(0,2,1):C.UVGC_173_19,(0,2,2):C.UVGC_173_20,(0,2,4):C.UVGC_173_21,(0,2,3):C.UVGC_210_65})

V_70 = CTVertex(name = 'V_70',
                type = 'UV',
                particles = [ P.d__tilde__, P.u, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.d, P.g], [P.g, P.u] ], [ [P.d, P.g, P.u] ] ],
                couplings = {(0,0,0):C.UVGC_195_32,(0,0,1):C.UVGC_195_33})

V_71 = CTVertex(name = 'V_71',
                type = 'UV',
                particles = [ P.s__tilde__, P.u, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.g, P.s], [P.g, P.u] ], [ [P.g, P.s, P.u] ] ],
                couplings = {(0,0,0):C.UVGC_197_36,(0,0,1):C.UVGC_197_37})

V_72 = CTVertex(name = 'V_72',
                type = 'UV',
                particles = [ P.d__tilde__, P.c, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.c, P.d, P.g] ], [ [P.c, P.g], [P.d, P.g] ] ],
                couplings = {(0,0,1):C.UVGC_191_24,(0,0,0):C.UVGC_191_25})

V_73 = CTVertex(name = 'V_73',
                type = 'UV',
                particles = [ P.s__tilde__, P.c, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.c, P.g], [P.g, P.s] ], [ [P.c, P.g, P.s] ] ],
                couplings = {(0,0,0):C.UVGC_193_28,(0,0,1):C.UVGC_193_29})

V_74 = CTVertex(name = 'V_74',
                type = 'UV',
                particles = [ P.b__tilde__, P.t, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.t] ], [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_212_67,(0,0,2):C.UVGC_212_68,(0,0,1):C.UVGC_212_69})

V_75 = CTVertex(name = 'V_75',
                type = 'UV',
                particles = [ P.t__tilde__, P.t, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_213_70,(0,1,0):C.UVGC_214_71})

V_76 = CTVertex(name = 'V_76',
                type = 'UV',
                particles = [ P.d__tilde__, P.d, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.UVGC_172_17,(0,1,0):C.UVGC_155_4,(0,2,0):C.UVGC_155_4})

V_77 = CTVertex(name = 'V_77',
                type = 'UV',
                particles = [ P.s__tilde__, P.s, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.UVGC_172_17,(0,1,0):C.UVGC_155_4,(0,2,0):C.UVGC_155_4})

V_78 = CTVertex(name = 'V_78',
                type = 'UV',
                particles = [ P.b__tilde__, P.b, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.UVGC_172_17,(0,1,0):C.UVGC_155_4,(0,2,0):C.UVGC_155_4})

V_79 = CTVertex(name = 'V_79',
                type = 'UV',
                particles = [ P.d__tilde__, P.d, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.b], [P.c], [P.d], [P.s], [P.u] ], [ [P.d, P.g] ], [ [P.g] ], [ [P.ghG] ], [ [P.t] ] ],
                couplings = {(0,0,1):C.UVGC_174_23,(0,1,0):C.UVGC_173_18,(0,1,2):C.UVGC_173_19,(0,1,3):C.UVGC_173_20,(0,1,4):C.UVGC_173_21,(0,1,1):C.UVGC_173_22,(0,2,0):C.UVGC_173_18,(0,2,2):C.UVGC_173_19,(0,2,3):C.UVGC_173_20,(0,2,4):C.UVGC_173_21,(0,2,1):C.UVGC_173_22})

V_80 = CTVertex(name = 'V_80',
                type = 'UV',
                particles = [ P.s__tilde__, P.s, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.b], [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.s] ], [ [P.t] ] ],
                couplings = {(0,0,3):C.UVGC_174_23,(0,1,0):C.UVGC_173_18,(0,1,1):C.UVGC_173_19,(0,1,2):C.UVGC_173_20,(0,1,4):C.UVGC_173_21,(0,1,3):C.UVGC_173_22,(0,2,0):C.UVGC_173_18,(0,2,1):C.UVGC_173_19,(0,2,2):C.UVGC_173_20,(0,2,4):C.UVGC_173_21,(0,2,3):C.UVGC_173_22})

V_81 = CTVertex(name = 'V_81',
                type = 'UV',
                particles = [ P.b__tilde__, P.b, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.b], [P.c], [P.d], [P.s], [P.u] ], [ [P.b, P.g] ], [ [P.g] ], [ [P.ghG] ], [ [P.t] ] ],
                couplings = {(0,0,1):C.UVGC_174_23,(0,1,0):C.UVGC_173_18,(0,1,2):C.UVGC_173_19,(0,1,3):C.UVGC_173_20,(0,1,4):C.UVGC_173_21,(0,1,1):C.UVGC_173_22,(0,2,0):C.UVGC_173_18,(0,2,2):C.UVGC_173_19,(0,2,3):C.UVGC_173_20,(0,2,4):C.UVGC_173_21,(0,2,1):C.UVGC_173_22})

V_82 = CTVertex(name = 'V_82',
                type = 'UV',
                particles = [ P.u__tilde__, P.d, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.d, P.g], [P.g, P.u] ], [ [P.d, P.g, P.u] ] ],
                couplings = {(0,0,0):C.UVGC_196_34,(0,0,1):C.UVGC_196_35})

V_83 = CTVertex(name = 'V_83',
                type = 'UV',
                particles = [ P.c__tilde__, P.d, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.c, P.d, P.g] ], [ [P.c, P.g], [P.d, P.g] ] ],
                couplings = {(0,0,1):C.UVGC_192_26,(0,0,0):C.UVGC_192_27})

V_84 = CTVertex(name = 'V_84',
                type = 'UV',
                particles = [ P.u__tilde__, P.s, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.g, P.s], [P.g, P.u] ], [ [P.g, P.s, P.u] ] ],
                couplings = {(0,0,0):C.UVGC_198_38,(0,0,1):C.UVGC_198_39})

V_85 = CTVertex(name = 'V_85',
                type = 'UV',
                particles = [ P.c__tilde__, P.s, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.c, P.g], [P.g, P.s] ], [ [P.c, P.g, P.s] ] ],
                couplings = {(0,0,0):C.UVGC_194_30,(0,0,1):C.UVGC_194_31})

V_86 = CTVertex(name = 'V_86',
                type = 'UV',
                particles = [ P.t__tilde__, P.b, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.t] ], [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_212_67,(0,0,2):C.UVGC_212_68,(0,0,1):C.UVGC_212_69})

V_87 = CTVertex(name = 'V_87',
                type = 'UV',
                particles = [ P.u__tilde__, P.u ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1, L.FF3, L.FF5 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.UVGC_171_16,(0,1,0):C.UVGC_154_3,(0,2,0):C.UVGC_154_3})

V_88 = CTVertex(name = 'V_88',
                type = 'UV',
                particles = [ P.c__tilde__, P.c ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1, L.FF3, L.FF5 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.UVGC_171_16,(0,1,0):C.UVGC_154_3,(0,2,0):C.UVGC_154_3})

V_89 = CTVertex(name = 'V_89',
                type = 'UV',
                particles = [ P.t__tilde__, P.t ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF2, L.FF3, L.FF4, L.FF5 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_211_66,(0,2,0):C.UVGC_211_66,(0,1,0):C.UVGC_208_63,(0,3,0):C.UVGC_208_63})

V_90 = CTVertex(name = 'V_90',
                type = 'UV',
                particles = [ P.d__tilde__, P.d ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1, L.FF3, L.FF5 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.UVGC_171_16,(0,1,0):C.UVGC_154_3,(0,2,0):C.UVGC_154_3})

V_91 = CTVertex(name = 'V_91',
                type = 'UV',
                particles = [ P.s__tilde__, P.s ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1, L.FF3, L.FF5 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.UVGC_171_16,(0,1,0):C.UVGC_154_3,(0,2,0):C.UVGC_154_3})

V_92 = CTVertex(name = 'V_92',
                type = 'UV',
                particles = [ P.b__tilde__, P.b ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1, L.FF3, L.FF5 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.UVGC_171_16,(0,1,0):C.UVGC_154_3,(0,2,0):C.UVGC_154_3})

V_93 = CTVertex(name = 'V_93',
                type = 'UV',
                particles = [ P.g, P.g ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VV1, L.VV3 ],
                loop_particles = [ [ [P.g] ], [ [P.ghG] ], [ [P.t] ] ],
                couplings = {(0,0,0):C.UVGC_200_41,(0,0,1):C.UVGC_200_42,(0,0,2):C.UVGC_200_43,(0,1,2):C.UVGC_199_40})

