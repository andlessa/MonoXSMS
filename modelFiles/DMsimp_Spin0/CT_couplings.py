# This file was automatically created by FeynRules 2.3.7
# Mathematica version: 9.0 for Linux x86 (64-bit) (November 20, 2012)
# Date: Mon 24 Aug 2015 14:17:57


from object_library import all_couplings, Coupling

from function_library import complexconjugate, re, im, csc, sec, acsc, asec, cot



R2GC_124_1 = Coupling(name = 'R2GC_124_1',
                      value = '(3*G**3)/(16.*cmath.pi**2)',
                      order = {'QCD':3})

R2GC_125_2 = Coupling(name = 'R2GC_125_2',
                      value = '-(complex(0,1)*G**2*MT**2)/(8.*cmath.pi**2)',
                      order = {'QCD':2})

R2GC_126_3 = Coupling(name = 'R2GC_126_3',
                      value = '-(complex(0,1)*G**2*MT*yt)/(8.*cmath.pi**2*cmath.sqrt(2))',
                      order = {'QCD':2,'QED':1})

R2GC_127_4 = Coupling(name = 'R2GC_127_4',
                      value = '(complex(0,1)*G**2*gSu33*MT*yt)/(8.*cmath.pi**2*cmath.sqrt(2))',
                      order = {'DMS':1,'QCD':2,'QED':1})

R2GC_128_5 = Coupling(name = 'R2GC_128_5',
                      value = '-(complex(0,1)*G**2*yt**2)/(16.*cmath.pi**2)',
                      order = {'QCD':2,'QED':2})

R2GC_129_6 = Coupling(name = 'R2GC_129_6',
                      value = '-(complex(0,1)*G**2*gPu33*yt**2)/(16.*cmath.pi**2)',
                      order = {'DMS':1,'QCD':2,'QED':2})

R2GC_130_7 = Coupling(name = 'R2GC_130_7',
                      value = '(complex(0,1)*G**2*gSu33*yt**2)/(16.*cmath.pi**2)',
                      order = {'DMS':1,'QCD':2,'QED':2})

R2GC_131_8 = Coupling(name = 'R2GC_131_8',
                      value = '-(ee*complex(0,1)*G**2*sw)/(18.*cw*cmath.pi**2)',
                      order = {'QCD':2,'QED':1})

R2GC_132_9 = Coupling(name = 'R2GC_132_9',
                      value = '-(ee*complex(0,1)*G**2)/(9.*cmath.pi**2)',
                      order = {'QCD':2,'QED':1})

R2GC_133_10 = Coupling(name = 'R2GC_133_10',
                       value = '(ee*complex(0,1)*G**2*sw)/(9.*cw*cmath.pi**2)',
                       order = {'QCD':2,'QED':1})

R2GC_139_11 = Coupling(name = 'R2GC_139_11',
                       value = '-(complex(0,1)*G**2*gPu33**2*yt**2)/(16.*cmath.pi**2) - (complex(0,1)*G**2*gSu33**2*yt**2)/(16.*cmath.pi**2)',
                       order = {'DMS':2,'QCD':2,'QED':2})

R2GC_140_12 = Coupling(name = 'R2GC_140_12',
                       value = '(ee**2*complex(0,1)*G**2)/(216.*cmath.pi**2)',
                       order = {'QCD':2,'QED':2})

R2GC_140_13 = Coupling(name = 'R2GC_140_13',
                       value = '(ee**2*complex(0,1)*G**2)/(54.*cmath.pi**2)',
                       order = {'QCD':2,'QED':2})

R2GC_141_14 = Coupling(name = 'R2GC_141_14',
                       value = '-(ee*complex(0,1)*G**3)/(144.*cmath.pi**2)',
                       order = {'QCD':3,'QED':1})

R2GC_141_15 = Coupling(name = 'R2GC_141_15',
                       value = '(ee*complex(0,1)*G**3)/(72.*cmath.pi**2)',
                       order = {'QCD':3,'QED':1})

R2GC_142_16 = Coupling(name = 'R2GC_142_16',
                       value = '(cw*ee**2*complex(0,1)*G**2)/(288.*cmath.pi**2*sw) - (ee**2*complex(0,1)*G**2*sw)/(864.*cw*cmath.pi**2)',
                       order = {'QCD':2,'QED':2})

R2GC_142_17 = Coupling(name = 'R2GC_142_17',
                       value = '(cw*ee**2*complex(0,1)*G**2)/(144.*cmath.pi**2*sw) - (5*ee**2*complex(0,1)*G**2*sw)/(432.*cw*cmath.pi**2)',
                       order = {'QCD':2,'QED':2})

R2GC_143_18 = Coupling(name = 'R2GC_143_18',
                       value = '-(cw*ee*complex(0,1)*G**3)/(192.*cmath.pi**2*sw) + (ee*complex(0,1)*G**3*sw)/(576.*cw*cmath.pi**2)',
                       order = {'QCD':3,'QED':1})

R2GC_143_19 = Coupling(name = 'R2GC_143_19',
                       value = '(cw*ee*complex(0,1)*G**3)/(192.*cmath.pi**2*sw) - (5*ee*complex(0,1)*G**3*sw)/(576.*cw*cmath.pi**2)',
                       order = {'QCD':3,'QED':1})

R2GC_144_20 = Coupling(name = 'R2GC_144_20',
                       value = '(-3*cw*ee*complex(0,1)*G**3)/(64.*cmath.pi**2*sw) - (3*ee*complex(0,1)*G**3*sw)/(64.*cw*cmath.pi**2)',
                       order = {'QCD':3,'QED':1})

R2GC_144_21 = Coupling(name = 'R2GC_144_21',
                       value = '(3*cw*ee*complex(0,1)*G**3)/(64.*cmath.pi**2*sw) + (3*ee*complex(0,1)*G**3*sw)/(64.*cw*cmath.pi**2)',
                       order = {'QCD':3,'QED':1})

R2GC_145_22 = Coupling(name = 'R2GC_145_22',
                       value = '(ee**2*complex(0,1)*G**2)/(288.*cmath.pi**2) + (cw**2*ee**2*complex(0,1)*G**2)/(192.*cmath.pi**2*sw**2) + (5*ee**2*complex(0,1)*G**2*sw**2)/(1728.*cw**2*cmath.pi**2)',
                       order = {'QCD':2,'QED':2})

R2GC_145_23 = Coupling(name = 'R2GC_145_23',
                       value = '-(ee**2*complex(0,1)*G**2)/(288.*cmath.pi**2) + (cw**2*ee**2*complex(0,1)*G**2)/(192.*cmath.pi**2*sw**2) + (17*ee**2*complex(0,1)*G**2*sw**2)/(1728.*cw**2*cmath.pi**2)',
                       order = {'QCD':2,'QED':2})

R2GC_146_24 = Coupling(name = 'R2GC_146_24',
                       value = '(cw*ee*complex(0,1)*G**2)/(12.*cmath.pi**2*sw) + (ee*complex(0,1)*G**2*sw)/(36.*cw*cmath.pi**2)',
                       order = {'QCD':2,'QED':1})

R2GC_147_25 = Coupling(name = 'R2GC_147_25',
                       value = '-(cw*ee*complex(0,1)*G**2)/(12.*cmath.pi**2*sw) + (ee*complex(0,1)*G**2*sw)/(36.*cw*cmath.pi**2)',
                       order = {'QCD':2,'QED':1})

R2GC_151_26 = Coupling(name = 'R2GC_151_26',
                       value = '(ee**2*complex(0,1)*G**2)/(96.*cmath.pi**2*sw**2)',
                       order = {'QCD':2,'QED':2})

R2GC_151_27 = Coupling(name = 'R2GC_151_27',
                       value = '(CKM2x1*ee**2*complex(0,1)*G**2*complexconjugate(CKM2x1))/(96.*cmath.pi**2*sw**2)',
                       order = {'QCD':2,'QED':2})

R2GC_151_28 = Coupling(name = 'R2GC_151_28',
                       value = '(CKM2x2*ee**2*complex(0,1)*G**2*complexconjugate(CKM2x2))/(96.*cmath.pi**2*sw**2)',
                       order = {'QCD':2,'QED':2})

R2GC_151_29 = Coupling(name = 'R2GC_151_29',
                       value = '(CKM1x1*ee**2*complex(0,1)*G**2*complexconjugate(CKM1x1))/(96.*cmath.pi**2*sw**2)',
                       order = {'QCD':2,'QED':2})

R2GC_151_30 = Coupling(name = 'R2GC_151_30',
                       value = '(CKM1x2*ee**2*complex(0,1)*G**2*complexconjugate(CKM1x2))/(96.*cmath.pi**2*sw**2)',
                       order = {'QCD':2,'QED':2})

R2GC_164_31 = Coupling(name = 'R2GC_164_31',
                       value = '-G**4/(192.*cmath.pi**2)',
                       order = {'QCD':4})

R2GC_164_32 = Coupling(name = 'R2GC_164_32',
                       value = 'G**4/(64.*cmath.pi**2)',
                       order = {'QCD':4})

R2GC_165_33 = Coupling(name = 'R2GC_165_33',
                       value = '-(complex(0,1)*G**4)/(192.*cmath.pi**2)',
                       order = {'QCD':4})

R2GC_165_34 = Coupling(name = 'R2GC_165_34',
                       value = '(complex(0,1)*G**4)/(64.*cmath.pi**2)',
                       order = {'QCD':4})

R2GC_166_35 = Coupling(name = 'R2GC_166_35',
                       value = '(complex(0,1)*G**4)/(192.*cmath.pi**2)',
                       order = {'QCD':4})

R2GC_166_36 = Coupling(name = 'R2GC_166_36',
                       value = '-(complex(0,1)*G**4)/(64.*cmath.pi**2)',
                       order = {'QCD':4})

R2GC_167_37 = Coupling(name = 'R2GC_167_37',
                       value = '-(complex(0,1)*G**4)/(48.*cmath.pi**2)',
                       order = {'QCD':4})

R2GC_168_38 = Coupling(name = 'R2GC_168_38',
                       value = '(complex(0,1)*G**4)/(288.*cmath.pi**2)',
                       order = {'QCD':4})

R2GC_168_39 = Coupling(name = 'R2GC_168_39',
                       value = '-(complex(0,1)*G**4)/(32.*cmath.pi**2)',
                       order = {'QCD':4})

R2GC_169_40 = Coupling(name = 'R2GC_169_40',
                       value = '-(complex(0,1)*G**4)/(16.*cmath.pi**2)',
                       order = {'QCD':4})

R2GC_170_41 = Coupling(name = 'R2GC_170_41',
                       value = '(-3*complex(0,1)*G**4)/(64.*cmath.pi**2)',
                       order = {'QCD':4})

R2GC_171_42 = Coupling(name = 'R2GC_171_42',
                       value = '(complex(0,1)*G**2)/(12.*cmath.pi**2)',
                       order = {'QCD':2})

R2GC_172_43 = Coupling(name = 'R2GC_172_43',
                       value = '(ee*complex(0,1)*G**2)/(18.*cmath.pi**2)',
                       order = {'QCD':2,'QED':1})

R2GC_174_44 = Coupling(name = 'R2GC_174_44',
                       value = '-(complex(0,1)*G**3)/(6.*cmath.pi**2)',
                       order = {'QCD':3})

R2GC_191_45 = Coupling(name = 'R2GC_191_45',
                       value = '-(CKM2x1*ee*complex(0,1)*G**2)/(6.*cmath.pi**2*sw*cmath.sqrt(2))',
                       order = {'QCD':2,'QED':1})

R2GC_192_46 = Coupling(name = 'R2GC_192_46',
                       value = '-(ee*complex(0,1)*G**2*complexconjugate(CKM2x1))/(6.*cmath.pi**2*sw*cmath.sqrt(2))',
                       order = {'QCD':2,'QED':1})

R2GC_193_47 = Coupling(name = 'R2GC_193_47',
                       value = '-(CKM2x2*ee*complex(0,1)*G**2)/(6.*cmath.pi**2*sw*cmath.sqrt(2))',
                       order = {'QCD':2,'QED':1})

R2GC_194_48 = Coupling(name = 'R2GC_194_48',
                       value = '-(ee*complex(0,1)*G**2*complexconjugate(CKM2x2))/(6.*cmath.pi**2*sw*cmath.sqrt(2))',
                       order = {'QCD':2,'QED':1})

R2GC_195_49 = Coupling(name = 'R2GC_195_49',
                       value = '-(CKM1x1*ee*complex(0,1)*G**2)/(6.*cmath.pi**2*sw*cmath.sqrt(2))',
                       order = {'QCD':2,'QED':1})

R2GC_196_50 = Coupling(name = 'R2GC_196_50',
                       value = '-(ee*complex(0,1)*G**2*complexconjugate(CKM1x1))/(6.*cmath.pi**2*sw*cmath.sqrt(2))',
                       order = {'QCD':2,'QED':1})

R2GC_197_51 = Coupling(name = 'R2GC_197_51',
                       value = '-(CKM1x2*ee*complex(0,1)*G**2)/(6.*cmath.pi**2*sw*cmath.sqrt(2))',
                       order = {'QCD':2,'QED':1})

R2GC_198_52 = Coupling(name = 'R2GC_198_52',
                       value = '-(ee*complex(0,1)*G**2*complexconjugate(CKM1x2))/(6.*cmath.pi**2*sw*cmath.sqrt(2))',
                       order = {'QCD':2,'QED':1})

R2GC_199_53 = Coupling(name = 'R2GC_199_53',
                       value = '(complex(0,1)*G**2)/(48.*cmath.pi**2)',
                       order = {'QCD':2})

R2GC_199_54 = Coupling(name = 'R2GC_199_54',
                       value = '(3*complex(0,1)*G**2)/(32.*cmath.pi**2)',
                       order = {'QCD':2})

R2GC_200_55 = Coupling(name = 'R2GC_200_55',
                       value = '-(complex(0,1)*G**2)/(16.*cmath.pi**2)',
                       order = {'QCD':2})

R2GC_201_56 = Coupling(name = 'R2GC_201_56',
                       value = 'G**3/(24.*cmath.pi**2)',
                       order = {'QCD':3})

R2GC_202_57 = Coupling(name = 'R2GC_202_57',
                       value = '(5*complex(0,1)*G**4)/(48.*cmath.pi**2)',
                       order = {'QCD':4})

R2GC_202_58 = Coupling(name = 'R2GC_202_58',
                       value = '(7*complex(0,1)*G**4)/(32.*cmath.pi**2)',
                       order = {'QCD':4})

R2GC_203_59 = Coupling(name = 'R2GC_203_59',
                       value = '(23*complex(0,1)*G**4)/(192.*cmath.pi**2)',
                       order = {'QCD':4})

R2GC_203_60 = Coupling(name = 'R2GC_203_60',
                       value = '(15*complex(0,1)*G**4)/(64.*cmath.pi**2)',
                       order = {'QCD':4})

R2GC_205_61 = Coupling(name = 'R2GC_205_61',
                       value = '(-17*complex(0,1)*G**4)/(64.*cmath.pi**2)',
                       order = {'QCD':4})

R2GC_206_62 = Coupling(name = 'R2GC_206_62',
                       value = '(-7*complex(0,1)*G**4)/(32.*cmath.pi**2)',
                       order = {'QCD':4})

R2GC_211_63 = Coupling(name = 'R2GC_211_63',
                       value = '(complex(0,1)*G**2*MT)/(6.*cmath.pi**2)',
                       order = {'QCD':2})

R2GC_212_64 = Coupling(name = 'R2GC_212_64',
                       value = '-(ee*complex(0,1)*G**2)/(6.*cmath.pi**2*sw*cmath.sqrt(2))',
                       order = {'QCD':2,'QED':1})

R2GC_215_65 = Coupling(name = 'R2GC_215_65',
                       value = '(G**2*yt)/(3.*cmath.pi**2)',
                       order = {'QCD':2,'QED':1})

R2GC_216_66 = Coupling(name = 'R2GC_216_66',
                       value = '-(G**2*yt)/(3.*cmath.pi**2)',
                       order = {'QCD':2,'QED':1})

R2GC_217_67 = Coupling(name = 'R2GC_217_67',
                       value = '(G**2*yt)/(3.*cmath.pi**2*cmath.sqrt(2))',
                       order = {'QCD':2,'QED':1})

R2GC_218_68 = Coupling(name = 'R2GC_218_68',
                       value = '(complex(0,1)*G**2*yt)/(3.*cmath.pi**2*cmath.sqrt(2))',
                       order = {'QCD':2,'QED':1})

R2GC_219_69 = Coupling(name = 'R2GC_219_69',
                       value = '-(G**2*gPu33*yt)/(3.*cmath.pi**2*cmath.sqrt(2))',
                       order = {'DMS':1,'QCD':2,'QED':1})

R2GC_220_70 = Coupling(name = 'R2GC_220_70',
                       value = '-(complex(0,1)*G**2*gSu33*yt)/(3.*cmath.pi**2*cmath.sqrt(2))',
                       order = {'DMS':1,'QCD':2,'QED':1})

UVGC_152_1 = Coupling(name = 'UVGC_152_1',
                      value = {-1:'(53*G**3)/(128.*cmath.pi**2)'},
                      order = {'QCD':3})

UVGC_153_2 = Coupling(name = 'UVGC_153_2',
                      value = {-1:'G**3/(32.*cmath.pi**2)'},
                      order = {'QCD':3})

UVGC_154_3 = Coupling(name = 'UVGC_154_3',
                      value = {-1:'-(complex(0,1)*G**2)/(12.*cmath.pi**2)'},
                      order = {'QCD':2})

UVGC_155_4 = Coupling(name = 'UVGC_155_4',
                      value = {-1:'-(ee*complex(0,1)*G**2)/(36.*cmath.pi**2)'},
                      order = {'QCD':2,'QED':1})

UVGC_157_5 = Coupling(name = 'UVGC_157_5',
                      value = {-1:'-(ee*complex(0,1)*G**2)/(18.*cmath.pi**2)'},
                      order = {'QCD':2,'QED':1})

UVGC_164_6 = Coupling(name = 'UVGC_164_6',
                      value = {-1:'(3*G**4)/(512.*cmath.pi**2)'},
                      order = {'QCD':4})

UVGC_164_7 = Coupling(name = 'UVGC_164_7',
                      value = {-1:'(-3*G**4)/(512.*cmath.pi**2)'},
                      order = {'QCD':4})

UVGC_165_8 = Coupling(name = 'UVGC_165_8',
                      value = {-1:'(3*complex(0,1)*G**4)/(512.*cmath.pi**2)'},
                      order = {'QCD':4})

UVGC_165_9 = Coupling(name = 'UVGC_165_9',
                      value = {-1:'(-3*complex(0,1)*G**4)/(512.*cmath.pi**2)'},
                      order = {'QCD':4})

UVGC_167_10 = Coupling(name = 'UVGC_167_10',
                       value = {-1:'-(complex(0,1)*G**4)/(128.*cmath.pi**2)'},
                       order = {'QCD':4})

UVGC_167_11 = Coupling(name = 'UVGC_167_11',
                       value = {-1:'(complex(0,1)*G**4)/(128.*cmath.pi**2)'},
                       order = {'QCD':4})

UVGC_168_12 = Coupling(name = 'UVGC_168_12',
                       value = {-1:'(-3*complex(0,1)*G**4)/(256.*cmath.pi**2)'},
                       order = {'QCD':4})

UVGC_168_13 = Coupling(name = 'UVGC_168_13',
                       value = {-1:'(3*complex(0,1)*G**4)/(256.*cmath.pi**2)'},
                       order = {'QCD':4})

UVGC_169_14 = Coupling(name = 'UVGC_169_14',
                       value = {-1:'-(complex(0,1)*G**4)/(24.*cmath.pi**2)'},
                       order = {'QCD':4})

UVGC_170_15 = Coupling(name = 'UVGC_170_15',
                       value = {-1:'(5*complex(0,1)*G**4)/(512.*cmath.pi**2)'},
                       order = {'QCD':4})

UVGC_171_16 = Coupling(name = 'UVGC_171_16',
                       value = {-1:'(complex(0,1)*G**2)/(12.*cmath.pi**2)'},
                       order = {'QCD':2})

UVGC_172_17 = Coupling(name = 'UVGC_172_17',
                       value = {-1:'(ee*complex(0,1)*G**2)/(36.*cmath.pi**2)'},
                       order = {'QCD':2,'QED':1})

UVGC_173_18 = Coupling(name = 'UVGC_173_18',
                       value = {-1:'(complex(0,1)*G**3)/(48.*cmath.pi**2)'},
                       order = {'QCD':3})

UVGC_173_19 = Coupling(name = 'UVGC_173_19',
                       value = {-1:'(-19*complex(0,1)*G**3)/(128.*cmath.pi**2)'},
                       order = {'QCD':3})

UVGC_173_20 = Coupling(name = 'UVGC_173_20',
                       value = {-1:'-(complex(0,1)*G**3)/(128.*cmath.pi**2)'},
                       order = {'QCD':3})

UVGC_173_21 = Coupling(name = 'UVGC_173_21',
                       value = {-1:'( 0 if MT else (complex(0,1)*G**3)/(48.*cmath.pi**2) )'},
                       order = {'QCD':3})

UVGC_173_22 = Coupling(name = 'UVGC_173_22',
                       value = {-1:'(complex(0,1)*G**3)/(12.*cmath.pi**2)'},
                       order = {'QCD':3})

UVGC_174_23 = Coupling(name = 'UVGC_174_23',
                       value = {-1:'(-13*complex(0,1)*G**3)/(48.*cmath.pi**2)'},
                       order = {'QCD':3})

UVGC_191_24 = Coupling(name = 'UVGC_191_24',
                       value = {-1:'(CKM2x1*ee*complex(0,1)*G**2)/(24.*cmath.pi**2*sw*cmath.sqrt(2))'},
                       order = {'QCD':2,'QED':1})

UVGC_191_25 = Coupling(name = 'UVGC_191_25',
                       value = {-1:'-(CKM2x1*ee*complex(0,1)*G**2)/(12.*cmath.pi**2*sw*cmath.sqrt(2))'},
                       order = {'QCD':2,'QED':1})

UVGC_192_26 = Coupling(name = 'UVGC_192_26',
                       value = {-1:'(ee*complex(0,1)*G**2*complexconjugate(CKM2x1))/(24.*cmath.pi**2*sw*cmath.sqrt(2))'},
                       order = {'QCD':2,'QED':1})

UVGC_192_27 = Coupling(name = 'UVGC_192_27',
                       value = {-1:'-(ee*complex(0,1)*G**2*complexconjugate(CKM2x1))/(12.*cmath.pi**2*sw*cmath.sqrt(2))'},
                       order = {'QCD':2,'QED':1})

UVGC_193_28 = Coupling(name = 'UVGC_193_28',
                       value = {-1:'(CKM2x2*ee*complex(0,1)*G**2)/(24.*cmath.pi**2*sw*cmath.sqrt(2))'},
                       order = {'QCD':2,'QED':1})

UVGC_193_29 = Coupling(name = 'UVGC_193_29',
                       value = {-1:'-(CKM2x2*ee*complex(0,1)*G**2)/(12.*cmath.pi**2*sw*cmath.sqrt(2))'},
                       order = {'QCD':2,'QED':1})

UVGC_194_30 = Coupling(name = 'UVGC_194_30',
                       value = {-1:'(ee*complex(0,1)*G**2*complexconjugate(CKM2x2))/(24.*cmath.pi**2*sw*cmath.sqrt(2))'},
                       order = {'QCD':2,'QED':1})

UVGC_194_31 = Coupling(name = 'UVGC_194_31',
                       value = {-1:'-(ee*complex(0,1)*G**2*complexconjugate(CKM2x2))/(12.*cmath.pi**2*sw*cmath.sqrt(2))'},
                       order = {'QCD':2,'QED':1})

UVGC_195_32 = Coupling(name = 'UVGC_195_32',
                       value = {-1:'(CKM1x1*ee*complex(0,1)*G**2)/(24.*cmath.pi**2*sw*cmath.sqrt(2))'},
                       order = {'QCD':2,'QED':1})

UVGC_195_33 = Coupling(name = 'UVGC_195_33',
                       value = {-1:'-(CKM1x1*ee*complex(0,1)*G**2)/(12.*cmath.pi**2*sw*cmath.sqrt(2))'},
                       order = {'QCD':2,'QED':1})

UVGC_196_34 = Coupling(name = 'UVGC_196_34',
                       value = {-1:'(ee*complex(0,1)*G**2*complexconjugate(CKM1x1))/(24.*cmath.pi**2*sw*cmath.sqrt(2))'},
                       order = {'QCD':2,'QED':1})

UVGC_196_35 = Coupling(name = 'UVGC_196_35',
                       value = {-1:'-(ee*complex(0,1)*G**2*complexconjugate(CKM1x1))/(12.*cmath.pi**2*sw*cmath.sqrt(2))'},
                       order = {'QCD':2,'QED':1})

UVGC_197_36 = Coupling(name = 'UVGC_197_36',
                       value = {-1:'(CKM1x2*ee*complex(0,1)*G**2)/(24.*cmath.pi**2*sw*cmath.sqrt(2))'},
                       order = {'QCD':2,'QED':1})

UVGC_197_37 = Coupling(name = 'UVGC_197_37',
                       value = {-1:'-(CKM1x2*ee*complex(0,1)*G**2)/(12.*cmath.pi**2*sw*cmath.sqrt(2))'},
                       order = {'QCD':2,'QED':1})

UVGC_198_38 = Coupling(name = 'UVGC_198_38',
                       value = {-1:'(ee*complex(0,1)*G**2*complexconjugate(CKM1x2))/(24.*cmath.pi**2*sw*cmath.sqrt(2))'},
                       order = {'QCD':2,'QED':1})

UVGC_198_39 = Coupling(name = 'UVGC_198_39',
                       value = {-1:'-(ee*complex(0,1)*G**2*complexconjugate(CKM1x2))/(12.*cmath.pi**2*sw*cmath.sqrt(2))'},
                       order = {'QCD':2,'QED':1})

UVGC_199_40 = Coupling(name = 'UVGC_199_40',
                       value = {-1:'( 0 if MT else -(complex(0,1)*G**2)/(24.*cmath.pi**2) ) + (complex(0,1)*G**2)/(24.*cmath.pi**2)',0:'( -(complex(0,1)*G**2*reglog(MT/MU_R))/(12.*cmath.pi**2) if MT else 0 )'},
                       order = {'QCD':2})

UVGC_200_41 = Coupling(name = 'UVGC_200_41',
                       value = {-1:'(3*complex(0,1)*G**2)/(64.*cmath.pi**2)'},
                       order = {'QCD':2})

UVGC_200_42 = Coupling(name = 'UVGC_200_42',
                       value = {-1:'(-3*complex(0,1)*G**2)/(64.*cmath.pi**2)'},
                       order = {'QCD':2})

UVGC_200_43 = Coupling(name = 'UVGC_200_43',
                       value = {-1:'( 0 if MT else (complex(0,1)*G**2)/(24.*cmath.pi**2) ) - (complex(0,1)*G**2)/(24.*cmath.pi**2)',0:'( (complex(0,1)*G**2*reglog(MT/MU_R))/(12.*cmath.pi**2) if MT else 0 )'},
                       order = {'QCD':2})

UVGC_201_44 = Coupling(name = 'UVGC_201_44',
                       value = {-1:'-G**3/(48.*cmath.pi**2)'},
                       order = {'QCD':3})

UVGC_201_45 = Coupling(name = 'UVGC_201_45',
                       value = {-1:'( 0 if MT else -G**3/(16.*cmath.pi**2) ) + G**3/(24.*cmath.pi**2)',0:'( -(G**3*reglog(MT/MU_R))/(12.*cmath.pi**2) if MT else 0 )'},
                       order = {'QCD':3})

UVGC_202_46 = Coupling(name = 'UVGC_202_46',
                       value = {-1:'(83*complex(0,1)*G**4)/(128.*cmath.pi**2)'},
                       order = {'QCD':4})

UVGC_202_47 = Coupling(name = 'UVGC_202_47',
                       value = {-1:'(3*complex(0,1)*G**4)/(128.*cmath.pi**2)'},
                       order = {'QCD':4})

UVGC_202_48 = Coupling(name = 'UVGC_202_48',
                       value = {-1:'( 0 if MT else -(complex(0,1)*G**4)/(12.*cmath.pi**2) ) + (complex(0,1)*G**4)/(12.*cmath.pi**2)',0:'( -(complex(0,1)*G**4*reglog(MT/MU_R))/(12.*cmath.pi**2) if MT else 0 )'},
                       order = {'QCD':4})

UVGC_203_49 = Coupling(name = 'UVGC_203_49',
                       value = {-1:'(335*complex(0,1)*G**4)/(512.*cmath.pi**2)'},
                       order = {'QCD':4})

UVGC_203_50 = Coupling(name = 'UVGC_203_50',
                       value = {-1:'(21*complex(0,1)*G**4)/(512.*cmath.pi**2)'},
                       order = {'QCD':4})

UVGC_204_51 = Coupling(name = 'UVGC_204_51',
                       value = {-1:'-(complex(0,1)*G**4)/(12.*cmath.pi**2)'},
                       order = {'QCD':4})

UVGC_204_52 = Coupling(name = 'UVGC_204_52',
                       value = {-1:'(13*complex(0,1)*G**4)/(512.*cmath.pi**2)'},
                       order = {'QCD':4})

UVGC_204_53 = Coupling(name = 'UVGC_204_53',
                       value = {-1:'( 0 if MT else -(complex(0,1)*G**4)/(12.*cmath.pi**2) )',0:'( -(complex(0,1)*G**4*reglog(MT/MU_R))/(12.*cmath.pi**2) if MT else 0 )'},
                       order = {'QCD':4})

UVGC_205_54 = Coupling(name = 'UVGC_205_54',
                       value = {-1:'(complex(0,1)*G**4)/(24.*cmath.pi**2)'},
                       order = {'QCD':4})

UVGC_205_55 = Coupling(name = 'UVGC_205_55',
                       value = {-1:'(-341*complex(0,1)*G**4)/(512.*cmath.pi**2)'},
                       order = {'QCD':4})

UVGC_205_56 = Coupling(name = 'UVGC_205_56',
                       value = {-1:'(-11*complex(0,1)*G**4)/(512.*cmath.pi**2)'},
                       order = {'QCD':4})

UVGC_205_57 = Coupling(name = 'UVGC_205_57',
                       value = {-1:'( 0 if MT else (complex(0,1)*G**4)/(12.*cmath.pi**2) ) - (complex(0,1)*G**4)/(24.*cmath.pi**2)',0:'( (complex(0,1)*G**4*reglog(MT/MU_R))/(12.*cmath.pi**2) if MT else 0 )'},
                       order = {'QCD':4})

UVGC_206_58 = Coupling(name = 'UVGC_206_58',
                       value = {-1:'(-83*complex(0,1)*G**4)/(128.*cmath.pi**2)'},
                       order = {'QCD':4})

UVGC_206_59 = Coupling(name = 'UVGC_206_59',
                       value = {-1:'(-5*complex(0,1)*G**4)/(128.*cmath.pi**2)'},
                       order = {'QCD':4})

UVGC_207_60 = Coupling(name = 'UVGC_207_60',
                       value = {-1:'(complex(0,1)*G**4)/(12.*cmath.pi**2)'},
                       order = {'QCD':4})

UVGC_207_61 = Coupling(name = 'UVGC_207_61',
                       value = {-1:'(-19*complex(0,1)*G**4)/(512.*cmath.pi**2)'},
                       order = {'QCD':4})

UVGC_207_62 = Coupling(name = 'UVGC_207_62',
                       value = {-1:'( 0 if MT else (complex(0,1)*G**4)/(12.*cmath.pi**2) )',0:'( (complex(0,1)*G**4*reglog(MT/MU_R))/(12.*cmath.pi**2) if MT else 0 )'},
                       order = {'QCD':4})

UVGC_208_63 = Coupling(name = 'UVGC_208_63',
                       value = {-1:'( (complex(0,1)*G**2)/(6.*cmath.pi**2) if MT else -(complex(0,1)*G**2)/(12.*cmath.pi**2) ) + (complex(0,1)*G**2)/(12.*cmath.pi**2)',0:'( (5*complex(0,1)*G**2)/(12.*cmath.pi**2) - (complex(0,1)*G**2*reglog(MT/MU_R))/(2.*cmath.pi**2) if MT else (complex(0,1)*G**2)/(12.*cmath.pi**2) ) - (complex(0,1)*G**2)/(12.*cmath.pi**2)'},
                       order = {'QCD':2})

UVGC_209_64 = Coupling(name = 'UVGC_209_64',
                       value = {-1:'( -(ee*complex(0,1)*G**2)/(9.*cmath.pi**2) if MT else (ee*complex(0,1)*G**2)/(18.*cmath.pi**2) )',0:'( (-5*ee*complex(0,1)*G**2)/(18.*cmath.pi**2) + (ee*complex(0,1)*G**2*reglog(MT/MU_R))/(3.*cmath.pi**2) if MT else -(ee*complex(0,1)*G**2)/(18.*cmath.pi**2) ) + (ee*complex(0,1)*G**2)/(18.*cmath.pi**2)'},
                       order = {'QCD':2,'QED':1})

UVGC_210_65 = Coupling(name = 'UVGC_210_65',
                       value = {-1:'( -(complex(0,1)*G**3)/(6.*cmath.pi**2) if MT else (complex(0,1)*G**3)/(12.*cmath.pi**2) )',0:'( (-5*complex(0,1)*G**3)/(12.*cmath.pi**2) + (complex(0,1)*G**3*reglog(MT/MU_R))/(2.*cmath.pi**2) if MT else -(complex(0,1)*G**3)/(12.*cmath.pi**2) ) + (complex(0,1)*G**3)/(12.*cmath.pi**2)'},
                       order = {'QCD':3})

UVGC_211_66 = Coupling(name = 'UVGC_211_66',
                       value = {-1:'( (complex(0,1)*G**2*MT)/(6.*cmath.pi**2) if MT else -(complex(0,1)*G**2*MT)/(12.*cmath.pi**2) ) + (complex(0,1)*G**2*MT)/(3.*cmath.pi**2)',0:'( (3*complex(0,1)*G**2*MT)/(4.*cmath.pi**2) - (complex(0,1)*G**2*MT*reglog(MT/MU_R))/cmath.pi**2 if MT else (complex(0,1)*G**2*MT)/(12.*cmath.pi**2) ) - (complex(0,1)*G**2*MT)/(12.*cmath.pi**2)'},
                       order = {'QCD':2})

UVGC_212_67 = Coupling(name = 'UVGC_212_67',
                       value = {-1:'(ee*complex(0,1)*G**2)/(24.*cmath.pi**2*sw*cmath.sqrt(2))'},
                       order = {'QCD':2,'QED':1})

UVGC_212_68 = Coupling(name = 'UVGC_212_68',
                       value = {-1:'( -(ee*complex(0,1)*G**2)/(12.*cmath.pi**2*sw*cmath.sqrt(2)) if MT else (ee*complex(0,1)*G**2)/(24.*cmath.pi**2*sw*cmath.sqrt(2)) )',0:'( (-5*ee*complex(0,1)*G**2)/(24.*cmath.pi**2*sw*cmath.sqrt(2)) + (ee*complex(0,1)*G**2*reglog(MT/MU_R))/(4.*cmath.pi**2*sw*cmath.sqrt(2)) if MT else -(ee*complex(0,1)*G**2)/(24.*cmath.pi**2*sw*cmath.sqrt(2)) ) + (ee*complex(0,1)*G**2)/(24.*cmath.pi**2*sw*cmath.sqrt(2))'},
                       order = {'QCD':2,'QED':1})

UVGC_212_69 = Coupling(name = 'UVGC_212_69',
                       value = {-1:'-(ee*complex(0,1)*G**2)/(12.*cmath.pi**2*sw*cmath.sqrt(2))'},
                       order = {'QCD':2,'QED':1})

UVGC_213_70 = Coupling(name = 'UVGC_213_70',
                       value = {-1:'( -(cw*ee*complex(0,1)*G**2)/(12.*cmath.pi**2*sw) + (ee*complex(0,1)*G**2*sw)/(36.*cw*cmath.pi**2) if MT else (cw*ee*complex(0,1)*G**2)/(24.*cmath.pi**2*sw) - (ee*complex(0,1)*G**2*sw)/(72.*cw*cmath.pi**2) ) - (cw*ee*complex(0,1)*G**2)/(24.*cmath.pi**2*sw) + (ee*complex(0,1)*G**2*sw)/(72.*cw*cmath.pi**2)',0:'( (-5*cw*ee*complex(0,1)*G**2)/(24.*cmath.pi**2*sw) + (5*ee*complex(0,1)*G**2*sw)/(72.*cw*cmath.pi**2) + (cw*ee*complex(0,1)*G**2*reglog(MT/MU_R))/(4.*cmath.pi**2*sw) - (ee*complex(0,1)*G**2*sw*reglog(MT/MU_R))/(12.*cw*cmath.pi**2) if MT else -(cw*ee*complex(0,1)*G**2)/(24.*cmath.pi**2*sw) + (ee*complex(0,1)*G**2*sw)/(72.*cw*cmath.pi**2) ) + (cw*ee*complex(0,1)*G**2)/(24.*cmath.pi**2*sw) - (ee*complex(0,1)*G**2*sw)/(72.*cw*cmath.pi**2)'},
                       order = {'QCD':2,'QED':1})

UVGC_214_71 = Coupling(name = 'UVGC_214_71',
                       value = {-1:'( (ee*complex(0,1)*G**2*sw)/(9.*cw*cmath.pi**2) if MT else -(ee*complex(0,1)*G**2*sw)/(18.*cw*cmath.pi**2) ) + (ee*complex(0,1)*G**2*sw)/(18.*cw*cmath.pi**2)',0:'( (5*ee*complex(0,1)*G**2*sw)/(18.*cw*cmath.pi**2) - (ee*complex(0,1)*G**2*sw*reglog(MT/MU_R))/(3.*cw*cmath.pi**2) if MT else (ee*complex(0,1)*G**2*sw)/(18.*cw*cmath.pi**2) ) - (ee*complex(0,1)*G**2*sw)/(18.*cw*cmath.pi**2)'},
                       order = {'QCD':2,'QED':1})

UVGC_215_72 = Coupling(name = 'UVGC_215_72',
                       value = {-1:'-(G**2*yt)/(24.*cmath.pi**2)'},
                       order = {'QCD':2,'QED':1})

UVGC_215_73 = Coupling(name = 'UVGC_215_73',
                       value = {-1:'( (G**2*yt)/(12.*cmath.pi**2) if MT else -(G**2*yt)/(24.*cmath.pi**2) )',0:'( (13*G**2*yt)/(24.*cmath.pi**2) - (3*G**2*yt*reglog(MT/MU_R))/(4.*cmath.pi**2) if MT else (G**2*yt)/(24.*cmath.pi**2) ) - (G**2*yt)/(24.*cmath.pi**2)'},
                       order = {'QCD':2,'QED':1})

UVGC_215_74 = Coupling(name = 'UVGC_215_74',
                       value = {-1:'(G**2*yt)/(3.*cmath.pi**2)'},
                       order = {'QCD':2,'QED':1})

UVGC_216_75 = Coupling(name = 'UVGC_216_75',
                       value = {-1:'(G**2*yt)/(24.*cmath.pi**2)'},
                       order = {'QCD':2,'QED':1})

UVGC_216_76 = Coupling(name = 'UVGC_216_76',
                       value = {-1:'( -(G**2*yt)/(12.*cmath.pi**2) if MT else (G**2*yt)/(24.*cmath.pi**2) )',0:'( (-13*G**2*yt)/(24.*cmath.pi**2) + (3*G**2*yt*reglog(MT/MU_R))/(4.*cmath.pi**2) if MT else -(G**2*yt)/(24.*cmath.pi**2) ) + (G**2*yt)/(24.*cmath.pi**2)'},
                       order = {'QCD':2,'QED':1})

UVGC_216_77 = Coupling(name = 'UVGC_216_77',
                       value = {-1:'-(G**2*yt)/(3.*cmath.pi**2)'},
                       order = {'QCD':2,'QED':1})

UVGC_217_78 = Coupling(name = 'UVGC_217_78',
                       value = {-1:'( (G**2*yt)/(6.*cmath.pi**2*cmath.sqrt(2)) if MT else -(G**2*yt)/(12.*cmath.pi**2*cmath.sqrt(2)) ) + (G**2*yt)/(3.*cmath.pi**2*cmath.sqrt(2))',0:'( (3*G**2*yt)/(4.*cmath.pi**2*cmath.sqrt(2)) - (G**2*yt*reglog(MT/MU_R))/(cmath.pi**2*cmath.sqrt(2)) if MT else (G**2*yt)/(12.*cmath.pi**2*cmath.sqrt(2)) ) - (G**2*yt)/(12.*cmath.pi**2*cmath.sqrt(2))'},
                       order = {'QCD':2,'QED':1})

UVGC_218_79 = Coupling(name = 'UVGC_218_79',
                       value = {-1:'( (complex(0,1)*G**2*yt)/(6.*cmath.pi**2*cmath.sqrt(2)) if MT else -(complex(0,1)*G**2*yt)/(12.*cmath.pi**2*cmath.sqrt(2)) ) + (complex(0,1)*G**2*yt)/(3.*cmath.pi**2*cmath.sqrt(2))',0:'( (3*complex(0,1)*G**2*yt)/(4.*cmath.pi**2*cmath.sqrt(2)) - (complex(0,1)*G**2*yt*reglog(MT/MU_R))/(cmath.pi**2*cmath.sqrt(2)) if MT else (complex(0,1)*G**2*yt)/(12.*cmath.pi**2*cmath.sqrt(2)) ) - (complex(0,1)*G**2*yt)/(12.*cmath.pi**2*cmath.sqrt(2))'},
                       order = {'QCD':2,'QED':1})

UVGC_219_80 = Coupling(name = 'UVGC_219_80',
                       value = {-1:'( -(G**2*gPu33*yt)/(6.*cmath.pi**2*cmath.sqrt(2)) if MT else (G**2*gPu33*yt)/(12.*cmath.pi**2*cmath.sqrt(2)) ) - (G**2*gPu33*yt)/(3.*cmath.pi**2*cmath.sqrt(2))',0:'( (-3*G**2*gPu33*yt)/(4.*cmath.pi**2*cmath.sqrt(2)) + (G**2*gPu33*yt*reglog(MT/MU_R))/(cmath.pi**2*cmath.sqrt(2)) if MT else -(G**2*gPu33*yt)/(12.*cmath.pi**2*cmath.sqrt(2)) ) + (G**2*gPu33*yt)/(12.*cmath.pi**2*cmath.sqrt(2))'},
                       order = {'DMS':1,'QCD':2,'QED':1})

UVGC_220_81 = Coupling(name = 'UVGC_220_81',
                       value = {-1:'( -(complex(0,1)*G**2*gSu33*yt)/(6.*cmath.pi**2*cmath.sqrt(2)) if MT else (complex(0,1)*G**2*gSu33*yt)/(12.*cmath.pi**2*cmath.sqrt(2)) ) - (complex(0,1)*G**2*gSu33*yt)/(3.*cmath.pi**2*cmath.sqrt(2))',0:'( (-3*complex(0,1)*G**2*gSu33*yt)/(4.*cmath.pi**2*cmath.sqrt(2)) + (complex(0,1)*G**2*gSu33*yt*reglog(MT/MU_R))/(cmath.pi**2*cmath.sqrt(2)) if MT else -(complex(0,1)*G**2*gSu33*yt)/(12.*cmath.pi**2*cmath.sqrt(2)) ) + (complex(0,1)*G**2*gSu33*yt)/(12.*cmath.pi**2*cmath.sqrt(2))'},
                       order = {'DMS':1,'QCD':2,'QED':1})

