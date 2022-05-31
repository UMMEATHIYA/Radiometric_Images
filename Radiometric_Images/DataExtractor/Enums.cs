using Newtonsoft.Json;
using Newtonsoft.Json.Converters;
using System;
using System.Runtime.Serialization;

namespace Radiometric_Images.DataExtractor
{
    internal class Enums
    {
        [JsonConverter(typeof(StringEnumConverter))]
        public enum TemperatureUnit
        {
            [EnumMember(Value = "Celsius")]
            Celsius,
            [EnumMember(Value = "Fahrenheit")]
            Fahrenheit,
            [EnumMember(Value = "Kelvin")]
            Kelvin,
            [EnumMember(Value = "Signal")]
            Signal
        }

        internal static TemperatureUnit Parse(Type type, object value)
        {
            throw new NotImplementedException();
        }
    }
}
