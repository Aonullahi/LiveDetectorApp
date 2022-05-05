import config
import pandas as pd
#============================================================================NG=========================================================================================

def sku_rule_NG(present_classes , *args):
    '''
    This function will:
        - Check if the key ABI SKUs are present in the chiller 
    
    Input: Dictionary with details about the bottles and whitespaces present in the chiller 
    Output: Boolean which is True when all stipulated conditions are met by the image

    '''
    cond1 = 'Budweiser' in present_classes
    cond2 = 'TrophyStout' in present_classes
    cond3 = 'Trophy' in present_classes
    cond4 = 'Hero' in present_classes
    cond5 = 'Chest' in present_classes

    if cond5:
        return True
    else:
        return (cond1 or cond2) and (cond3 or cond4)


def whitespace_percent_NG(full_output, present_classes):
    '''
    This function will use the inference output to calculate the amount
    of whitespace in the ciller 

    Input: Inference results and classes present in the chiller 
    Output: Percentage of whitespace in the chiller

    '''   
    area_list = full_output['instances'].pred_boxes.area().tolist()

    glass_area = 0
    whitespace_area = 0
    DChiller_area = 0

    for i in range(len(present_classes)):
        if present_classes[i] == '2DChiller':
            DChiller_area += area_list[i]

        elif present_classes[i] == 'Glass': 
            glass_area += area_list[i]
  
        elif present_classes[i] == 'WhiteSpaces':
            whitespace_area += area_list[i]

    if 'Chest' in present_classes:
        return 0
  
    if '2DChiller' in present_classes:
        return round((whitespace_area/(0.5 * DChiller_area)) * 100) 

    elif glass_area == 0:
        return 0 
  
    else:
        return round((whitespace_area/(0.5 * glass_area)) * 100)


def whitespace_rule_NG(img_output, whitespace_percent):
    '''
    This function will:
        - check if the whitespace condition has been satisfied

    Input: inference output and whitespace percentage
    Output: Boolean
    
    '''
    if 'Chest' in img_output.keys():
        return False
    else:
        return whitespace_percent >= config.max_whitespace_area["NG"] 


def fine_tune_NG(img_output, percentage_whitespace):
    '''
    This function will:
        - edit the infernce output based on some expected behaviours
    Input: inference output and whitespace percentage
    Output: edited inference output and whitespace percentage
    
    '''
    if list(img_output.keys()) == ["WhiteSpaces", "Glass"] or list(img_output.keys()) == ["Glass","WhiteSpaces"]:
        if (percentage_whitespace > 0) and (percentage_whitespace <= 50):
            percentage_whitespace = 0
        elif percentage_whitespace > 100:
            percentage_whitespace = 100

    elif 'Chest' in img_output.keys():
        img_output['Chest'] = 1

    elif '2DChiller' in img_output.keys():
        img_output['Glass'] = 1
        
    if 'Glass' in img_output.keys():
        img_output['Glass'] = 1   

    return img_output, percentage_whitespace


def count_rule_NG(img_output):
    '''
    This function will:
        - check if the number of bottles meet the required condition
    Input: inference output 
    Output: Boolean
    '''
    
    num_bottles = 0
 
    for sku in img_output.keys():
        if sku in config.sku_classes["NG"]:
            num_bottles += img_output[sku]

    if 'Chest' in img_output.keys():
        return True

    elif '2DChiller' in img_output.keys():
        return num_bottles >= config.double_door_min_bottles["NG"]

    elif 'Glass' in img_output.keys():
        return num_bottles >= config.single_door_min_bottles["NG"]

    else:
        return False


#=====================================================================================TZ===============================================================================

def sku_rule_TZ(present_classes, region, *args):
    '''
    This function will:
        - Check if the key ABI SKUs are present in the chiller 
    
    Input: Dictionary with details about the bottles and whitespaces present in the chiller 
    Output: Boolean which is True when all stipulated conditions are met by the image

    '''
    
    cond1 = 'CastleLiteCAN' in present_classes
    cond2 = 'CastleLiteRGB' in present_classes

    cond3 = 'CastleMilkStoutRGB' in present_classes
    cond4 = 'CastleRGB' in present_classes
    cond5 = 'CastleCAN' in present_classes

    cond6 = 'KilimanjaroCAN' in present_classes
    cond7 = 'KilimanjaroRGB' in present_classes

    cond8 = 'BalimiRGB' in present_classes

    cond9 = 'SafariRGB' in present_classes
    cond10 = 'SafariRGB' in present_classes

    cond11 = 'ReddsRGB' in present_classes
    cond12 = 'ReddsCAN' in present_classes

    cond13 = 'EagleRGB' in present_classes

    cond14 = 'BingwaRGB' in present_classes
    cond15 = 'GrandMaltCAN' in present_classes

    if region == "Central":
        return (cond1 or cond2) and (cond6 or cond7) and (cond9 or cond10)  and (cond11 or cond12) and cond15

    elif region == "North East":
        return (cond1 or cond2) and (cond9 or cond10)  and (cond6 or cond7) and cond13 and cond15 

    elif region == "North West":
        return (cond1 or cond2) and (cond9 or cond10)  and (cond6 or cond7) and cond8 and cond13 and cond15

    elif region == "South":
        return (cond1 or cond2) and (cond9 or cond10)  and (cond6 or cond7) and cond14 and cond15

    else:
        return (cond1 or cond2) and (cond6 or cond7) and (cond8) and (cond9 or cond10)  and (cond11 or cond12)


def whitespace_percent_TZ(full_output, present_classes):
    '''
    This function will use the inference output to calculate the amount
    of whitespace in the ciller 

    Input: Inference results and classes present in the chiller 
    Output: Percentage of whitespace in the chiller

    '''   
    area_list = full_output['instances'].pred_boxes.area().tolist()

    glass_area = 0
    whitespace_area = 0
    DChiller_area = 0

    for i in range(len(present_classes)):
        if present_classes[i] == '2DChiller':
            DChiller_area += area_list[i]

        elif present_classes[i] == 'Cooler': 
            glass_area += area_list[i]
  
        elif present_classes[i] == 'WhiteSpace':
            whitespace_area += area_list[i]

    if 'Chest' in present_classes:
        return 0
  
    if '2DChiller' in present_classes:
        return round((whitespace_area/(0.5 * DChiller_area)) * 100) 

    elif glass_area == 0:
        return 0 
  
    else:
        return round((whitespace_area/(0.5 * glass_area)) * 100)


def whitespace_rule_TZ(img_output, whitespace_percent):
    '''
    This function will:
        - check if the whitespace condition has been satisfied

    Input: inference output and whitespace percentage
    Output: Boolean
    
    '''
    if 'Chest' in img_output.keys():
        return False
    else:
        return whitespace_percent >= config.max_whitespace_area["TZ"] 


def count_rule_TZ(img_output):
    '''
    This function will:
        - check if the number of bottles meet the required condition
    Input: inference output 
    Output: Boolean
    '''
    
    num_bottles = 0
 
    for sku in img_output.keys():
        if sku in config.sku_classes["TZ"]:
            num_bottles += img_output[sku]

    if 'Chest' in img_output.keys():
        return True

    elif '2DChiller' in img_output.keys():
        return num_bottles >= config.double_door_min_bottles["TZ"]

    elif 'Cooler' in img_output.keys():
        return num_bottles >= config.single_door_min_bottles["TZ"]

    else:
        return False

#=====================================================================================UG===============================================================================

def sku_rule_UG(present_classes, region, *args):
    '''
    This function will:
        - Check if the key ABI SKUs are present in the chiller 
    
    Input: Dictionary with details about the bottles and whitespaces present in the chiller 
    Output: Boolean which is True when all stipulated conditions are met by the image

    '''

    cond1 = 'Castlelite' in present_classes
    cond2 = 'CastleliteCan' in present_classes

    cond3 = 'CastleMilkStout' in present_classes

    cond4 = 'Club' in present_classes

    cond5 = 'NileStout' in present_classes

    cond6 = 'EagleLager' in present_classes

    cond7 = 'EagleDark' in present_classes

    cond8 = 'NileSpecial' in present_classes

    
    if region == "East":
        return (cond1 or cond2) and (cond4) and (cond5) and (cond6 or cond7 or cond8)  

    elif region == "West":
        return (cond1 or cond2) and (cond4) and (cond5) and (cond6 or cond7 or cond8)
   
    else:
        return (cond1 or cond2) and (cond4) and (cond5) and (cond6 or cond7 or cond8)


def whitespace_percent_UG(full_output, present_classes):
    '''
    This function will use the inference output to calculate the amount
    of whitespace in the ciller 

    Input: Inference results and classes present in the chiller 
    Output: Percentage of whitespace in the chiller

    '''   
    area_list = full_output['instances'].pred_boxes.area().tolist()

    glass_area = 0
    whitespace_area = 0
    DChiller_area = 0

    for i in range(len(present_classes)):
        if present_classes[i] == '2DChiller':
            DChiller_area += area_list[i]

        elif present_classes[i] == 'Cooler': 
            glass_area += area_list[i]
  
        elif present_classes[i] == 'WhiteSpace':
            whitespace_area += area_list[i]

    if 'Chest' in present_classes:
        return 0
  
    if '2DChiller' in present_classes:
        return round((whitespace_area/(0.5 * DChiller_area)) * 100) 

    elif glass_area == 0:
        return 0 
  
    else:
        return round((whitespace_area/(0.5 * glass_area)) * 100)


def whitespace_rule_UG(img_output, whitespace_percent):
    '''
    This function will:
        - check if the whitespace condition has been satisfied

    Input: inference output and whitespace percentage
    Output: Boolean
    
    '''
    if 'Chest' in img_output.keys():
        return False
    else:
        return whitespace_percent >= config.max_whitespace_area["UG"] 


def count_rule_UG(img_output):
    '''
    This function will:
        - check if the number of bottles meet the required condition
    Input: inference output 
    Output: Boolean
    '''
    
    num_bottles = 0
 
    for sku in img_output.keys():
        if sku in config.sku_classes["UG"]:
            num_bottles += img_output[sku]

    if 'Chest' in img_output.keys():
        return True

    elif '2DChiller' in img_output.keys():
        return num_bottles >= config.double_door_min_bottles["UG"]

    elif 'Cooler' in img_output.keys():
        return num_bottles >= config.single_door_min_bottles["UG"]

    else:
        return False


#=====================================================================================MZ===============================================================================

def sku_rule_MZ(present_classes, region, *args):
    '''
    This function will:
        - Check if the key ABI SKUs are present in the chiller 

    Input: Dictionary with details about the bottles and whitespaces present in the chiller 
    Output: Boolean which is True when all stipulated conditions are met by the image

    '''
    excecution_rule = []
    if "ce" in region.lower():
        for i in config.rules_cluster["MZ"]['ce']:
            focus_brands = list(pd.read_excel("MZ_info.xlsx", sheet_name="task")[i])
            check_list = [i for i in list(set(present_classes)) if i in focus_brands]
            if check_list != []:
                excecution_rule.append(True)
            else:
                excecution_rule.append(False)

    elif "no" in region.lower():
        for i in config.rules_cluster["MZ"]['no']:
            focus_brands = list(pd.read_excel("MZ_info.xlsx", sheet_name="task")[i])
            check_list = [i for i in list(set(present_classes)) if i in focus_brands]
            if check_list != []:
                excecution_rule.append(True)
            else:
                excecution_rule.append(False)

    elif "so" in region.lower():
        for i in config.rules_cluster["MZ"]['so']:
            focus_brands = list(pd.read_excel("MZ_info.xlsx", sheet_name="task")[i])
            check_list = [i for i in list(set(present_classes)) if i in focus_brands]
            if check_list != []:
                excecution_rule.append(True)
            else:
                excecution_rule.append(False)

    else:
        excecution_rule.append(False)
    
    return all(excecution_rule)


def whitespace_percent_MZ(full_output, present_classes):
    '''
    This function will use the inference output to calculate the amount
    of whitespace in the ciller 

    Input: Inference results and classes present in the chiller 
    Output: Percentage of whitespace in the chiller

    '''   
    area_list = full_output['instances'].pred_boxes.area().tolist()

    glass_area = 0
    whitespace_area = 0
    DChiller_area = 0

    for i in range(len(present_classes)):
        if present_classes[i] == '2DChiller':
            DChiller_area += area_list[i]

        elif present_classes[i] == 'Cooler': 
            glass_area += area_list[i]
  
        elif present_classes[i] == 'WhiteSpace':
            whitespace_area += area_list[i]

    if 'Chest' in present_classes:
        return 0
  
    if '2DChiller' in present_classes:
        return round((whitespace_area/(0.5 * DChiller_area)) * 100) 

    elif glass_area == 0:
        return 0 
  
    else:
        return round((whitespace_area/(0.5 * glass_area)) * 100)


def whitespace_rule_MZ(img_output, whitespace_percent):
    '''
    This function will:
        - check if the whitespace condition has been satisfied

    Input: inference output and whitespace percentage
    Output: Boolean
    
    '''
    if 'Chest' in img_output.keys():
        return False
    else:
        return whitespace_percent >= config.max_whitespace_area["MZ"] 


def count_rule_MZ(img_output):
    '''
    This function will:
        - check if the number of bottles meet the required condition
    Input: inference output 
    Output: Boolean
    '''
    
    num_bottles = 0
 
    for sku in img_output.keys():
        if "pack" in sku.lower():
            num_bottles += 6

        elif sku in config.sku_classes["MZ"]:
            num_bottles += img_output[sku]

    if 'Chest' in img_output.keys():
        return True

    elif '2DChiller' in img_output.keys():
        return num_bottles >= config.double_door_min_bottles["MZ"]

    elif 'Cooler' in img_output.keys():
        return num_bottles >= config.single_door_min_bottles["MZ"]

    else:
        return False